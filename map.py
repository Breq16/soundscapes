import mido

print("Helper to map MIDI CC in Ableton Live")
print("Enter MIDI map edit mode (Cmd+M) now!")

port = mido.open_output("MIDI CC map helper by breq", virtual=True)

try:
    channel = int(input("Enter MIDI channel (1-16): ")) - 1
    control = int(input("Enter MIDI control (0-127): "))

    port.send(
        mido.Message("control_change", channel=channel, control=control, value=42)
    )
finally:
    port.close()
