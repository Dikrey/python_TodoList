import os
import datetime

# ------------------------
# Created By: Raihan_official0307
# Github: Dikrey
# Jangan Dihapus!!! 
# Hargai Pembuatnya!!! 
# ------------------------
# Script ini adalah aplikasi To-Do List sederhana dengan fitur-fitur:
# - Menambahkan tugas
# - Menampilkan tugas
# - Menghapus tugas
# - Menyimpan tugas ke file
# - Pencarian tugas
# - Melihat tugas berdasarkan tanggal
# - Mengatur prioritas tugas
# ------------------------

def show_created_by():
    print("=" * 50)
    print(" " * 10 + "Created By: Raihan_official0307".center(30))
    print("=" * 50)
    print(" " * 15 + "Script Aplikasi To-Do List".center(20))
    print("=" * 50)
    print("\n")

class TodoList:
    def __init__(self, filename="todo.txt"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        tasks = []
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    task_details = line.strip().split(" | ")
                    if len(task_details) == 4:
                        tasks.append({
                            "task": task_details[0], 
                            "date": task_details[1], 
                            "created_at": task_details[2],
                            "priority": task_details[3]
                        })
        return tasks

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task['task']} | {task['date']} | {task['created_at']} | {task['priority']}\n")

    def show_tasks(self):
        if not self.tasks:
            print("\n[INFO] Tidak ada tugas dalam daftar.")
        else:
            print("\n[Daftar Tugas Anda]:\n")
            print(f"{'No':<5} {'Tugas':<30} {'Tanggal':<15} {'Dibuat Pada':<20} {'Prioritas':<10}")
            print("=" * 80)
            for idx, task in enumerate(sorted(self.tasks, key=lambda x: x['created_at'], reverse=True), 1):
                print(f"{idx:<5} {task['task']:<30} {task['date']:<15} {task['created_at']:<20} {task['priority']:<10}")
            print("=" * 80)

    def add_task(self, task, date, priority):
        created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.tasks.append({"task": task, "date": date, "created_at": created_at, "priority": priority})
        self.save_tasks()
        print(f"[INFO] Tugas '{task}' dengan prioritas '{priority}' telah ditambahkan.")

    def remove_task(self, task_index):
        try:
            removed_task = self.tasks.pop(task_index - 1)
            self.save_tasks()
            print(f"[INFO] Tugas '{removed_task['task']}' telah dihapus.")
        except IndexError:
            print("[ERROR] Indeks tugas tidak valid.")

    def search_task(self, keyword):
        print("\n[Hasil Pencarian]:")
        print(f"{'No':<5} {'Tugas':<30} {'Tanggal':<15} {'Dibuat Pada':<20} {'Prioritas':<10}")
        print("=" * 80)
        found = False
        for idx, task in enumerate(self.tasks, 1):
            if keyword.lower() in task['task'].lower():
                print(f"{idx:<5} {task['task']:<30} {task['date']:<15} {task['created_at']:<20} {task['priority']:<10}")
                found = True
        if not found:
            print("[INFO] Tidak ada tugas yang cocok dengan kata kunci.")

    def show_tasks_by_date(self, target_date):
        print(f"\n[Tugas untuk Tanggal {target_date}]:")
        print(f"{'No':<5} {'Tugas':<30} {'Tanggal':<15} {'Dibuat Pada':<20} {'Prioritas':<10}")
        print("=" * 80)
        found = False
        for idx, task in enumerate(self.tasks, 1):
            if task['date'] == target_date:
                print(f"{idx:<5} {task['task']:<30} {task['date']:<15} {task['created_at']:<20} {task['priority']:<10}")
                found = True
        if not found:
            print("[INFO] Tidak ada tugas pada tanggal tersebut.")
# ------------------------
# Created By: Raihan_official0307
# Github: Dikrey
# Jangan Dihapus!!! 
# Hargai Pembuatnya!!! 
# ------------------------
def show_menu():
    print("\n--- To-Do List ---")
    print("1. Lihat Daftar Tugas")
    print("2. Tambah Tugas")
    print("3. Hapus Tugas")
    print("4. Pencarian Tugas")
    print("5. Lihat Tugas Berdasarkan Tanggal")
    print("6. Keluar")

def valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def valid_priority(priority):
    return priority.lower() in ["rendah", "sedang", "tinggi"]

def main():
    show_created_by()  # Menampilkan informasi pembuat ketika program dimulai
    
    todo_list = TodoList()
    # ------------------------
# Created By: Raihan_official0307
# Github: Dikrey
# Jangan Dihapus!!! 
# Hargai Pembuatnya!!! 
# ------------------------
    while True:
        show_menu()
        choice = input("Pilih opsi (1-6): ")

        if choice == "1":
            todo_list.show_tasks()
        elif choice == "2":
            task = input("Masukkan tugas: ").strip()
            if not task:
                print("[ERROR] Tugas tidak boleh kosong!")
                continue

            date = input("Masukkan tanggal tugas (YYYY-MM-DD): ").strip()
            if not valid_date(date):
                print("[ERROR] Format tanggal tidak valid. Gunakan YYYY-MM-DD.")
                continue

            priority = input("Masukkan prioritas (rendah, sedang, tinggi): ").strip().lower()
            if not valid_priority(priority):
                print("[ERROR] Prioritas tidak valid. Pilih dari 'rendah', 'sedang', atau 'tinggi'.")
                continue
#Raihan_official0307
            todo_list.add_task(task, date, priority)
        elif choice == "3":
            todo_list.show_tasks()
            try:
                task_index = int(input("Masukkan nomor tugas yang akan dihapus: "))
                todo_list.remove_task(task_index)
            except ValueError:
                print("[ERROR] Masukkan angka yang valid.")
        elif choice == "4":
            keyword = input("Masukkan kata kunci untuk pencarian: ").strip()
            todo_list.search_task(keyword)
        elif choice == "5":
            target_date = input("Masukkan tanggal tugas yang ingin dilihat (YYYY-MM-DD): ").strip()
            if not valid_date(target_date):
                print("[ERROR] Format tanggal tidak valid. Gunakan YYYY-MM-DD.")
                continue
            todo_list.show_tasks_by_date(target_date)
        elif choice == "6":
            print("[INFO] Terima kasih! Sampai jumpa!")
            break
        else:
            print("[ERROR] Opsi tidak valid. Silakan pilih antara 1-6.")

if __name__ == "__main__":
    main()
# ------------------------
# Created By: Raihan_official0307
# Github: Dikrey
# Jangan Dihapus!!! 
# Hargai Pembuatnya!!! 
# ------------------------
