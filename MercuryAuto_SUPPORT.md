# Mercury Auto — Support

Mercury Auto 0.3 provides generic read-only OBD readings, emissions trouble codes, supported VIN responses and local reports. It is independent of BMW, ISTA, BimmerCode and BimmerLink. It does not currently perform BMW module coding, service resets, ECU flashing, map installation or iDrive application installation.

## Connecting
- Use an iOS-compatible serial ELM adapter. The original vLinker BM Bluetooth model is not supported on iOS by its manufacturer; BM+ BLE and BM Wi-Fi are iOS variants. Compatibility with this application still requires physical validation.
- For Wi-Fi, join the adapter network in iPhone Settings and enter the IP address and TCP port from its manual.
- For BLE, select the discovered adapter and enter the exact service, write and notify UUIDs documented by the manufacturer. No validated vLinker BLE profile is preconfigured.
- Grant Bluetooth/local-network access when prompted. The app disconnects when moved to the background. Use diagnosis while parked.
- “Unavailable” can mean an unsupported PID, response framing or adapter configuration; it does not prove that the vehicle has no faults.

## Reports
Save a diagnostic session from the Diagnostics tab. Find saved reports in Reports. Export omits VIN by default. Demo readings are explicitly labelled and do not represent a vehicle test.

## Contact
Open a support issue at https://github.com/valentinnedelcu1974-arch/iEnergy-iData-iOS/issues with the title “Mercury Auto support”. Include the iOS version, app version, adapter model/firmware and a brief description. Do not post passwords, private keys, full VINs or personal information. Support messages submitted through GitHub are public.

Privacy policy: [Mercury Auto Privacy](MercuryAuto_PRIVACY.md).
