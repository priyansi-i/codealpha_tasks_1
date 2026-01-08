from scapy.all import sniff, IP

def packet_callback(packet):
    if IP in packet:
        print(
            f"Source: {packet[IP].src} | "
            f"Destination: {packet[IP].dst} | "
            f"Protocol: {packet[IP].proto}"
        )

sniff(filter="ip", prn=packet_callback, store=False, count=20)
