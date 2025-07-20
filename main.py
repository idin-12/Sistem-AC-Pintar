# ============================
# Sistem AC Pintar Rumah John

# 🔧 Input status sensor
is_hot = True            # True jika suhu panas, False jika tidak panas
window_closed = True     # True jika jendela tertutup, False jika terbuka
someone_home = True      # True jika ada orang di rumah, False jika kosong

# ⚡ Logika Sistem AC
if is_hot and window_closed and someone_home:
    ac_status = "MENYALA"
else:
    ac_status = "MATI"

# 🔊 Output status AC
print("=== Sistem AC Pintar Rumah John ===")
print(f"Suhu panas: {is_hot}")
print(f"Jendela tertutup: {window_closed}")
print(f"Ada orang di rumah: {someone_home}")
print(f"Status AC: {ac_status}")
