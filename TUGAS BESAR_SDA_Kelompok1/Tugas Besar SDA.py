from datetime import datetime
import tkinter as tk
from tkinter import Label, PhotoImage, messagebox
from tkinter import ttk

window = tk.Tk()  # create a window widget

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
# window.state("zoomed")
window.title("Sistem Informasi Perpustakaan")
window.geometry("1200x600")


page1 = tk.Frame(window)
page2 = tk.Frame(window)
page3 = tk.Frame(window)
page4 = tk.Frame(window)
page5 = tk.Frame(window)
page6 = tk.Frame(window)

for frame in (page1, page2, page3, page4, page5, page6):
    frame.grid(row=0, column=0, sticky='nsew')


def show_frame(frame):
    frame.tkraise()


show_frame(page1)

# ============================Page 1==================================
bg = PhotoImage(file="START1.png")

# Show image using label
label1 = Label(page1, image=bg)
label1.place(x=-70, y=15)

tombol = tk.Button(window, text=" START ", font=(
    "MONOSPACE", 15), activebackground="blue", command=lambda: show_frame(page2))
tombol.place(x=330, y=400)

# ==============================Page 2================================
bg2 = PhotoImage(file="admin.png")

# Show image using label
label3 = Label(page2, image=bg2)
label3.place(x=500, y=150)

next_button = tk.Button(page2, text="ADMIN", command=lambda: show_frame(
    page3), font=(20), activebackground='blue')
next_button.place(x=300, y=300)

next_button = tk.Button(page2, text="USER", command=lambda: show_frame(
    page6), font=(20), activebackground='blue')
next_button.place(x=300, y=450)


# ============================== Page 3 ===============================
page3.config(background="white")
logo1 = tk.PhotoImage(file="login_admin.png")

pag2_label = tk.Label(page3, text='SIGN IN', font=(
    'Arial', 30, 'bold'), bg="white", fg='black')
pag2_label.place(x=90, y=50)

pag3_label = tk.Label(page3, text='', font=(
    'Arial', 30, 'bold'), bg="white", fg='black', image=logo1, compound="right")
pag3_label.place(x=400, y=50)


def cek_login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "12345":
        label_error.config(text="")
        page2.pack_forget()
        show_frame(page4)

    else:
        messagebox.showinfo("WARNING", " password anda salah")


# Membuat label dan entry untuk username
label_username = tk.Label(master=page3, text="Username", font=(
    "Argent", 15), fg='black', bg="#FFC948")
label_username.place(x=100, y=140)

entry_username = tk.Entry(master=page3, bg="#7CFAFF")
entry_username.place(x=100, y=170)

# Membuat label dan entry untuk password
label_password = tk.Label(master=page3, text="Password",
                          font=("Argent", 15), bg="#FFC948")
label_password.place(x=100, y=210)

entry_password = tk.Entry(master=page3, bg="#7CFAFF", show="*")
entry_password.place(x=100, y=240)

# Membuat button untuk login
button_login = tk.Button(master=page3, text=" Login ", font=(
    "MONOSPACE", 15), activebackground='blue', command=cek_login)
button_login.place(x=100, y=280)

# Membuat label untuk pesan error
label_error = tk.Label(master=page3)
label_error.place(x=100, y=280)

button_login = tk.Button(master=page3, text=" Back< ", font=(
    "MONOSPACE", 15), activebackground='blue', command=lambda: show_frame(page2))
button_login.place(x=100, y=600)


# ============================== Page 4 ===========================================
bg1 = PhotoImage(file="tambah3.png")

# Show image using label
label2 = Label(page4, image=bg1)
label2.place(x=260, y=0)

# Daftar buku beserta informasi ketersediaan, nama pengarang, dan letak rak buku
books = [
    {"judul": "1984", "ketersediaan": True,
        "pengarang": "George Orwell", "rak_buku": "C3"},
    {"judul": "Animal Farm", "ketersediaan": True,
        "pengarang": "George Orwell", "rak_buku": "D4"},
    {"judul": "Brave New World", "ketersediaan": True,
        "pengarang": "Aldous Huxley", "rak_buku": "G7"},
    {"judul": "Lord of the Flies", "ketersediaan": False,
        "pengarang": "William Golding", "rak_buku": "I9"},
    {"judul": "Pride and Prejudice", "ketersediaan": True,
        "pengarang": "Jane Austen", "rak_buku": "E5"},
    {"judul": "The Adventures of Huckleberry Finn", "ketersediaan": True,
        "pengarang": "Mark Twain", "rak_buku": "H8"},
    {"judul": "The Catcher in the Rye", "ketersediaan": False,
        "pengarang": "J.D. Salinger", "rak_buku": "F6"},
    {"judul": "The Grapes of Wrath", "ketersediaan": True,
        "pengarang": "John Steinbeck", "rak_buku": "J10"},
    {"judul": "The Great Gatsby", "ketersediaan": True,
        "pengarang": "F. Scott Fitzgerald", "rak_buku": "A1"},
    {"judul": "To Kill a Mockingbird", "ketersediaan": False,
        "pengarang": "Harper Lee", "rak_buku": "B2"}
]

# Fungsi untuk melakukan pencarian buku dengan binary search


def binary_search(books, target):
    left = 0
    right = len(books) - 1

    while left <= right:
        mid = (left + right) // 2
        if books[mid]["judul"] == target:
            return mid
        elif books[mid]["judul"] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Fungsi untuk menampilkan hasil pencarian


def show_result():
    target_book = entry.get()
    index = binary_search(books, target_book)
    if index == -1:
        message.config(text=f"{target_book} tidak ditemukan.")
    else:
        book = books[index]
        if book["ketersediaan"]:
            ketersediaan = "tersedia"
        else:
            ketersediaan = "tidak tersedia"
        message.config(
            text=f"Judul: {book['judul']}\nKetersediaan: {ketersediaan}\nPengarang: {book['pengarang']}\nRak Buku: {book['rak_buku']}")

# Fungsi untuk menambahkan buku baru


def add_book():
    new_book = {
        "judul": title_entry.get(),
        "ketersediaan": True if availability_combobox.get() == "Tersedia" else False,
        "pengarang": author_entry.get(),
        "rak_buku": shelf_entry.get()
    }
    books.append(new_book)
    # Urutkan kembali array
    books.sort(key=lambda x: x["judul"])
    # Update Treeview
    update_treeview()

    # Clear input fields
    title_entry.delete(0, tk.END)
    availability_combobox.set("Tersedia")
    author_entry.delete(0, tk.END)
    shelf_entry.delete(0, tk.END)

    # Pastikan bahwa array selalu terurut setelah setiap perubahan
    books.sort(key=lambda x: x["judul"])

# Fungsi untuk mengubah ketersediaan buku


def toggle_availability():
    # Cari indeks buku yang akan diubah ketersediaannya
    target_book = treeview.selection()[0]
    index = int(target_book.split("_")[1])

    # Ubah ketersediaan buku
    books[index]["ketersediaan"] = not books[index]["ketersediaan"]

    # Update Treeview
    update_treeview()

# Fungsi untuk menghapus buku


def delete_book():
    # Cari indeks buku yang akan dihapus
    target_book = treeview.selection()[0]
    index = int(target_book.split("_")[1])

    # Hapus buku dari daftar
    del books[index]

    # Update Treeview
    update_treeview()

# Fungsi untuk mengupdate Treeview


def update_treeview():
    # Hapus semua item di Treeview
    treeview.delete(*treeview.get_children())

    # Tambahkan buku-buku dari daftar ke Treeview
    for i, book in enumerate(books):
        ketersediaan = "Tersedia" if book["ketersediaan"] else "Tidak Tersedia"
        treeview.insert(parent="", index=i, iid=f"book_{i}", text="", values=(
            book["judul"], ketersediaan, book["pengarang"], book["rak_buku"]))


# Membuat Treeview
treeview = ttk.Treeview(page4, columns=(
    "judul", "ketersediaan", "pengarang", "rak_buku"), show="headings")
treeview.heading("judul", text="Judul")
treeview.heading("ketersediaan", text="Ketersediaan")
treeview.heading("pengarang", text="Pengarang")
treeview.heading("rak_buku", text="Rak Buku")
treeview.pack()

# Tambahkan buku-buku dari daftar ke Treeview
for i, book in enumerate(books):
    ketersediaan = "Tersedia" if book["ketersediaan"] else "Tidak Tersedia"
    treeview.insert(parent="", index=i, iid=f"book_{i}", text="", values=(
        book["judul"], ketersediaan, book["pengarang"], book["rak_buku"]))

# Membuat form untuk menambahkan buku baru
form_label = tk.Label(page4, text="Penambahan Buku Baru",
                      bg="light yellow", fg='black')
form_label.place(x=550, y=400)

title_label = tk.Label(page4, text="Judul:", bg="light blue", fg='black')
title_label.place(x=300, y=475)

title_entry = tk.Entry(page4)
title_entry.place(x=250, y=500)

availability_label = tk.Label(
    page4, text="Ketersediaan:", bg="light blue", fg='black')
availability_label.place(x=450, y=475)

availability_combobox = ttk.Combobox(
    page4, values=["Tersedia", "Tidak Tersedia"])
availability_combobox.set("Tersedia")
availability_combobox.place(x=425, y=500)

author_label = tk.Label(page4, text="Pengarang:", bg="light blue", fg='black')
author_label.place(x=675, y=475)

author_entry = tk.Entry(page4)
author_entry.place(x=655, y=500)

shelf_label = tk.Label(page4, text="Rak Buku:", bg="light blue", fg='black')
shelf_label.place(x=905, y=475)

shelf_entry = tk.Entry(page4)
shelf_entry.place(x=880, y=500)

add_button = tk.Button(page4, text="Tambah Buku",
                       bg="light yellow", fg='black', command=add_book)
add_button.place(x=570, y=550)

# Membuat tombol untuk mengubah ketersediaan buku
toggle_button = tk.Button(
    page4, text="Ubah Ketersediaan", command=toggle_availability)
toggle_button.place(x=250, y=240)

delete_button = tk.Button(page4, text="Hapus Buku", command=delete_book)
delete_button.place(x=900, y=240)

pinjam_button = tk.Button(page4, text="Peminjaman Buku -->", command=lambda: show_frame(
    page5), font=("Arial", 12), activebackground='blue')
pinjam_button.place(x=940, y=650)


back_button = tk.Button(master=page4, text=" Back< ", font=(
    "MONOSPACE", 15), activebackground='blue', command=lambda: show_frame(page3))
back_button.place(x=100, y=650)

# =============================Page 5====================================

bg5 = PhotoImage(file="PINJAM.png")

# Show image using label
label4 = ttk.Label(page5, image=bg5)
label4.place(x=30, y=45)

# Membuat array untuk menyimpan data peminjam
peminjam = []

# Fungsi untuk menambahkan peminjam baru


def tambah_peminjam():
    nama = nama_entry.get()
    npm = npm_entry.get()
    tgl_pinjam = datetime.strptime(tgl_pinjam_entry.get(), '%d/%m/%Y')
    tgl_kembali = datetime.strptime(tgl_kembali_entry.get(), '%d/%m/%Y')
    judul_buku = judul_buku_entry.get()

    peminjam.append({"nama": nama, "npm": npm,
                    "tgl_pinjam": tgl_pinjam, "tgl_kembali": tgl_kembali, "judul_buku": judul_buku})
    message.config(text="Data peminjam berhasil ditambahkan.")

# Fungsi untuk menghapus data peminjam


def hapus_peminjam():
    nama = nama_entry3.get()

    for data in peminjam:
        if data["nama"] == nama:
            peminjam.remove(data)
            message.config(text="Data peminjam berhasil dihapus.")
            result.config(text="")
            return

    message.config(text="Data peminjam tidak ditemukan.")
    result.config(text="")

# Fungsi untuk menampilkan daftar peminjam


def tampilkan_peminjam():
    if len(peminjam) == 0:
        message.config(text="Belum ada data peminjam.")
        result.config(text="")
    else:
        message.config(text="")
        text = ""
        for data in peminjam:
            text += f"Nama: {data['nama']}\nNPM: {data['npm']}\nJudul Buku: {data['judul_buku']}\nTgl. Pinjam: {data['tgl_pinjam'].strftime('%d/%m/%Y')}\nTgl. Kembali: {data['tgl_kembali'].strftime('%d/%m/%Y')}\n\n"
        result.config(text=text)


# Membuat notebook
notebook = ttk.Notebook(page5)
notebook.pack(pady=10)

# Membuat tab tambah peminjam
tambah_tab = ttk.Frame(notebook)
notebook.add(tambah_tab, text="Tambah Peminjam")

nama_label = ttk.Label(tambah_tab, text="Nama:")
nama_label.pack(pady=5)

nama_entry = ttk.Entry(tambah_tab)
nama_entry.pack(pady=5)

npm_label = ttk.Label(tambah_tab, text="NPM:")
npm_label.pack(pady=5)

npm_entry = ttk.Entry(tambah_tab)
npm_entry.pack(pady=5)

judul_buku_label = ttk.Label(tambah_tab, text="Judul Buku:")
judul_buku_label.pack(pady=5)

judul_buku_entry = ttk.Entry(tambah_tab)
judul_buku_entry.pack(pady=5)

tgl_pinjam_label = ttk.Label(tambah_tab, text="Tgl. Pinjam (dd/mm/yyyy):")
tgl_pinjam_label.pack(pady=5)

tgl_pinjam_entry = ttk.Entry(tambah_tab)
tgl_pinjam_entry.pack(pady=5)

tgl_kembali_label = ttk.Label(tambah_tab, text="Tgl. Kembali (dd/mm/yyyy):")
tgl_kembali_label.pack(pady=5)

tgl_kembali_entry = ttk.Entry(tambah_tab)
tgl_kembali_entry.pack(pady=5)

tambah_button = ttk.Button(tambah_tab, text="Tambah", command=tambah_peminjam)
tambah_button.pack(pady=10)

# Membuat tab hapus peminjam
hapus_tab = ttk.Frame(notebook)
notebook.add(hapus_tab, text="Hapus Peminjam")

nama_label3 = ttk.Label(hapus_tab, text="Nama:")
nama_label3.pack(pady=5)

nama_entry3 = ttk.Entry(hapus_tab)
nama_entry3.pack(pady=5)

hapus_button = ttk.Button(hapus_tab, text="Hapus", command=hapus_peminjam)
hapus_button.pack(pady=10)

# Membuat tab tampilkan peminjam
tampilkan_tab = ttk.Frame(notebook)
notebook.add(tampilkan_tab, text="Tampilkan Peminjam")

tampilkan_button = ttk.Button(
    tampilkan_tab, text="Tampilkan", command=tampilkan_peminjam)
tampilkan_button.pack(pady=10)

result = ttk.Label(tampilkan_tab, text="")
result.pack(pady=10)

# Membuat label untuk pesan
message = ttk.Label(page5, text="")
message.pack(pady=10)

back_button = tk.Button(master=page5, text=" Back< ", font=(
    "MONOSPACE", 15), activebackground='blue', command=lambda: show_frame(page4))
back_button.place(x=100, y=600)

# ===================================Page 6====================================
bg4 = PhotoImage(file="CARI.png")

# Show image using label
label4 = Label(page6, image=bg4)
label4.place(x=360, y=110)


# Daftar buku beserta informasi ketersediaan, nama pengarang, dan letak rak buku
books = [
    {"judul": "1984", "ketersediaan": True,
        "pengarang": "George Orwell", "rak_buku": "C3"},
    {"judul": "Animal Farm", "ketersediaan": True,
        "pengarang": "George Orwell", "rak_buku": "D4"},
    {"judul": "Brave New World", "ketersediaan": True,
        "pengarang": "Aldous Huxley", "rak_buku": "G7"},
    {"judul": "Lord of the Flies", "ketersediaan": False,
        "pengarang": "William Golding", "rak_buku": "I9"},
    {"judul": "Pride and Prejudice", "ketersediaan": True,
        "pengarang": "Jane Austen", "rak_buku": "E5"},
    {"judul": "The Adventures of Huckleberry Finn", "ketersediaan": True,
        "pengarang": "Mark Twain", "rak_buku": "H8"},
    {"judul": "The Catcher in the Rye", "ketersediaan": False,
        "pengarang": "J.D. Salinger", "rak_buku": "F6"},
    {"judul": "The Grapes of Wrath", "ketersediaan": True,
        "pengarang": "John Steinbeck", "rak_buku": "J10"},
    {"judul": "The Great Gatsby", "ketersediaan": True,
        "pengarang": "F. Scott Fitzgerald", "rak_buku": "A1"},
    {"judul": "To Kill a Mockingbird", "ketersediaan": False,
        "pengarang": "Harper Lee", "rak_buku": "B2"}
]

# Fungsi untuk melakukan pencarian buku dengan binary search


def binary_search(books, target):
    left = 0
    right = len(books) - 1

    while left <= right:
        mid = (left + right) // 2
        if books[mid]["judul"] == target:
            return mid
        elif books[mid]["judul"] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Fungsi untuk menampilkan hasil pencarian dalam bentuk tabel


def show_result():
    target_book = entry.get()
    index = binary_search(books, target_book)
    if index == -1:
        message.config(text=f"{target_book} tidak ditemukan.")
    else:
        book = books[index]
        if book["ketersediaan"]:
            ketersediaan = "tersedia"
        else:
            ketersediaan = "tidak tersedia"

        table = ttk.Treeview(page6, columns=(
            "Ketersediaan", "Pengarang", "Rak Buku"))
        table.heading("#0", text="Judul")
        table.heading("Ketersediaan", text="Ketersediaan")
        table.heading("Pengarang", text="Pengarang")
        table.heading("Rak Buku", text="Rak Buku")
        table.insert("", "end", text=book["judul"], values=(
            ketersediaan, book["pengarang"], book["rak_buku"]))
        table.place(x=250, y=300)


label = tk.Label(page6, text="Masukkan judul buku yang ingin dicari:")
label.place(x=520, y=100)

entry = tk.Entry(page6)
entry.place(x=570, y=125)

button = tk.Button(page6, text="Cari", command=show_result)
button.place(x=610, y=150)

message = tk.Label(page6, text="")
message.place(x=620, y=180)


back_button = tk.Button(master=page6, text=" Back< ", font=(
    "MONOSPACE", 15), activebackground='blue', command=lambda: show_frame(page2))
back_button.place(x=100, y=650)

window.mainloop()
