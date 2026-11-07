import SwiftUI
import WebKit
import UIKit

@main
struct IEnergyApp: App {
    var body: some Scene {
        WindowGroup { WebsiteScreen() }
    }
}

@MainActor
final class WebsiteModel: NSObject, ObservableObject, WKNavigationDelegate, WKUIDelegate {
    static let home = URL(string: "https://ienergy-idata.com")!
    @Published var loading = false
    @Published var canGoBack = false
    @Published var failure: String?
    let webView: WKWebView

    override init() {
        let configuration = WKWebViewConfiguration()
        configuration.websiteDataStore = .default()
        webView = WKWebView(frame: .zero, configuration: configuration)
        super.init()
        webView.navigationDelegate = self
        webView.uiDelegate = self
        webView.allowsBackForwardNavigationGestures = true
        webView.scrollView.refreshControl = UIRefreshControl()
        webView.scrollView.refreshControl?.addTarget(self, action: #selector(refresh), for: .valueChanged)
        goHome()
    }

    func goHome() {
        failure = nil
        webView.load(URLRequest(url: Self.home))
    }

    @objc func refresh() {
        failure = nil
        if webView.url == nil { goHome() } else { webView.reload() }
    }

    func webView(_ webView: WKWebView, didStartProvisionalNavigation navigation: WKNavigation!) {
        loading = true
        failure = nil
    }

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        finish()
    }

    func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) {
        failed(error)
    }

    func webView(_ webView: WKWebView, didFailProvisionalNavigation navigation: WKNavigation!, withError error: Error) {
        failed(error)
    }

    func webViewWebContentProcessDidTerminate(_ webView: WKWebView) {
        loading = false
        failure = "Pagina trebuie reîncărcată."
    }

    private func finish() {
        loading = false
        canGoBack = webView.canGoBack
        webView.scrollView.refreshControl?.endRefreshing()
    }

    private func failed(_ error: Error) {
        finish()
        if (error as NSError).code != NSURLErrorCancelled {
            failure = "Nu se poate încărca pagina. Verifică internetul și încearcă din nou."
        }
    }

    func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction,
                 decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {
        guard let url = navigationAction.request.url else {
            decisionHandler(.cancel)
            return
        }
        let host = url.host?.lowercased() ?? ""
        let internalSite = host == "ienergy-idata.com" || host == "www.ienergy-idata.com"
        if internalSite && url.scheme == "https" {
            decisionHandler(.allow)
        } else if navigationAction.navigationType == .linkActivated || navigationAction.targetFrame == nil {
            decisionHandler(.cancel)
            if ["https", "http", "mailto", "tel"].contains(url.scheme?.lowercased() ?? "") {
                UIApplication.shared.open(url)
            }
        } else if url.scheme == "https" || url.scheme == "about" {
            // Permit secure embedded content used by the website.
            decisionHandler(.allow)
        } else {
            decisionHandler(.cancel)
        }
    }

    func webView(_ webView: WKWebView, createWebViewWith configuration: WKWebViewConfiguration,
                 for navigationAction: WKNavigationAction, windowFeatures: WKWindowFeatures) -> WKWebView? {
        guard let url = navigationAction.request.url else { return nil }
        if url.host == Self.home.host {
            webView.load(URLRequest(url: url))
        }
        return nil
    }
}

struct WebsiteScreen: View {
    @StateObject private var model = WebsiteModel()

    var body: some View {
        VStack(spacing: 0) {
            HStack {
                Image(systemName: "bolt.circle.fill").foregroundStyle(.cyan)
                Text("iEnergy & iData").font(.headline)
                Spacer()
                if model.loading { ProgressView().controlSize(.small) }
            }
            .padding(.horizontal).padding(.vertical, 10)

            ZStack {
                WebsiteView(model: model)
                if let failure = model.failure {
                    VStack(spacing: 16) {
                        Image(systemName: "wifi.exclamationmark").font(.largeTitle)
                        Text(failure).multilineTextAlignment(.center)
                        Button("Reîncearcă") { model.refresh() }
                            .buttonStyle(.borderedProminent)
                    }
                    .padding(28)
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
                    .background(.background)
                }
            }

            Divider()
            HStack {
                Button { model.webView.goBack() } label: {
                    Label("Înapoi", systemImage: "chevron.left")
                }
                .disabled(!model.canGoBack)
                Spacer()
                Button { model.goHome() } label: {
                    Label("Acasă", systemImage: "house")
                }
                Spacer()
                Button { model.refresh() } label: {
                    Image(systemName: "arrow.clockwise").accessibilityLabel("Reîncarcă")
                }
                ShareLink(item: model.webView.url ?? WebsiteModel.home) {
                    Image(systemName: "square.and.arrow.up")
                }
                .padding(.leading, 12)
            }
            .padding(.horizontal).padding(.vertical, 12)
        }
        .tint(.blue)
    }
}

struct WebsiteView: UIViewRepresentable {
    let model: WebsiteModel
    func makeUIView(context: Context) -> WKWebView { model.webView }
    func updateUIView(_ uiView: WKWebView, context: Context) {}
}
