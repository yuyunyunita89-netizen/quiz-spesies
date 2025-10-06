import streamlit as st
import random

# ----------------------------
# Daftar spesies: (nama umum, nama ilmiah)
# ----------------------------
species_list = [
    ("Singa", "Panthera leo"),
    ("Harimau", "Panthera tigris"),
    ("Gajah Afrika", "Loxodonta africana"),
    ("Gajah Asia", "Elephas maximus"),
    ("Kucing", "Felis catus"),
    ("Anjing", "Canis lupus familiaris"),
    ("Manusia", "Homo sapiens"),
    ("Sapi", "Bos taurus"),
    ("Kuda", "Equus ferus caballus"),
    ("Ayam", "Gallus gallus domesticus"),
    ("Panda", "Ailuropoda melanoleuca"),
    ("Gorila", "Gorilla gorilla"),
    ("Orangutan", "Pongo pygmaeus"),
    ("Lumba-lumba", "Delphinus delphis"),
    ("Kangguru", "Macropus rufus"),
    ("Beruang Kutub", "Ursus maritimus"),
    ("Burung Hantu", "Strigiformes"),
    ("Ikan Paus Biru", "Balaenoptera musculus"),
    ("Kuda Nil", "Hippopotamus amphibius"),
    ("Zebra", "Equus zebra"),
    ("Elang", "Aquila chrysaetos"),
    ("Buaya", "Crocodylus porosus"),
    ("Penguin Kaisar", "Aptenodytes forsteri"),
    ("Rubah", "Vulpes vulpes"),
    ("Serigala", "Canis lupus"),
    ("Banteng", "Bos javanicus"),
    ("Komodo", "Varanus komodoensis"),
    ("Burung Merak", "Pavo cristatus"),
    ("Katak", "Anura"),
    ("Iguana", "Iguana iguana"),
    ("Kucing Hutan", "Prionailurus bengalensis"),
    ("Ular Sanca", "Python reticulatus"),
    ("Burung Kolibri", "Trochilidae"),
    ("Belalang", "Caelifera"),
    ("Kupu-kupu", "Lepidoptera"),
    ("Cacing Tanah", "Lumbricus terrestris"),
    ("Lebah Madu", "Apis mellifera"),
    ("Gagak", "Corvus corax"),
    ("Tikus", "Rattus rattus"),
    ("Tupai", "Sciuridae"),
    ("Jerapah", "Giraffa camelopardalis"),
    ("Rusa", "Cervus elaphus"),
    ("Kelinci", "Oryctolagus cuniculus"),
    ("Babi", "Sus scrofa domesticus"),
    ("Burung Unta", "Struthio camelus"),
    ("Badak", "Rhinoceros unicornis"),
    ("Tarsius", "Tarsius tarsier"),
    ("Belut Listrik", "Electrophorus electricus"),
    ("Trenggiling", "Manis javanica"),
    ("Burung Cendrawasih", "Paradisaea"),
]

# ----------------------------
# Inisialisasi Session State
# ----------------------------
if 'questions' not in st.session_state:
    st.session_state.questions = random.sample(species_list, 50)
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answers = []

# ----------------------------
# Fungsi untuk menampilkan soal
# ----------------------------
def show_question():
    q_num = st.session_state.current + 1
    common_name, correct_answer = st.session_state.questions[st.session_state.current]

    # Ambil 3 pilihan lain sebagai pengecoh
    choices = [correct_answer]
    while len(choices) < 4:
        option = random.choice(species_list)[1]
        if option not in choices:
            choices.append(option)
    random.shuffle(choices)

    st.subheader(f"Soal {q_num} dari 50")
    st.write(f"Apa nama ilmiah dari **{common_name}**?")

    choice = st.radio("Pilih jawaban Anda:", choices, key=f"q_{q_num}")
    if st.button("Kirim Jawaban"):
        if choice == correct_answer:
            st.success("✅ Benar!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Salah. Jawaban yang benar: {correct_answer}")

        st.session_state.answers.append((common_name, correct_answer, choice))
        st.session_state.current += 1
        st.experimental_rerun()

# ----------------------------
# Halaman utama
# ----------------------------
st.title("🧠 Kuis: Tebak Nama Ilmiah Spesies")
st.write("Jawablah 50 soal pilihan ganda tentang nama ilmiah spesies hewan.")

if st.session_state.current < 50:
    show_question()
else:
    st.success("🎉 Kuis Selesai!")
    st.write(f"Skor Anda: **{st.session_state.score} / 50**")
    st.write(f"Persentase: **{st.session_state.score * 2}%**")

    with st.expander("📋 Lihat Jawaban Anda"):
        for idx, (common, correct, chosen) in enumerate(st.session_state.answers, 1):
            result = "✅" if correct == chosen else "❌"
            st.write(f"{idx}. {common} - Jawaban Anda: _{chosen}_ {result} (Benar: _{correct}_)")

    if st.button("🔁 Main Lagi"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.experimental_rerun()
