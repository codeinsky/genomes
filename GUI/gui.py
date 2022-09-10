import tkinter
from ttkwidgets import CheckboxTreeview
from tkinter import filedialog
import guiSelectRefGenome
import load_downloaded_genomes
import scanning_genomes

top = tkinter.Tk()
top.geometry('900x500')


def browsefunc():
    filename = filedialog.askopenfilename(filetypes=(("fasta files", "*.fasta"), ("All files", "*.*")))
    file_path.config(text=filename)
    print(filename)


def removeLoadedProbe():
    file_path.config(text="")


def selectRefGenomes():
    guiSelectRefGenome.selectRefGenomes(top)


def update_ref_genomes():
    print("updating data")
    treeRef.delete(*treeRef.get_children())
    local_items = load_downloaded_genomes.load_downloaded_genomes()
    for index, item in enumerate(local_items):
        treeRef.insert("", "end", index, text=index, values=(item, "comment"))
    print("updating data")


def start_scan():
    # check if ref. genomes and probe is correct
    if "fasta" in file_path.cget("text") and len(treeRef.get_checked()) > 0:
        print("ready to start")
        genomes_ids = treeRef.get_checked()
        probe_path = (file_path.cget("text"))
        ref_genomes = []
        for id in genomes_ids:
            ref_genomes.append(treeRef.item(id)['values'][0])
        scanning_genomes.scan_genomes(ref_genomes, probe_path)
    else:
        print("Please select data or probe file")


#  Genome frame
# *********************************************
genome_frame = tkinter.Frame(top, borderwidth=5, highlightbackground="black", highlightthickness=1)
genome_frame.grid(row=0, column=0, sticky="N", pady=10, padx=10)
tkinter.Label(genome_frame, text="Reference genome list").grid(row=2, column=0)
global treeRef
treeRef = CheckboxTreeview(genome_frame, column=("1", "2"), show=("headings", "tree"))
treeRef.heading("#0", text="GenomeID")
treeRef.column("#0", minwidth=0, width=80)
treeRef.grid(row=3, column=0)
treeRef.heading("1", text="Name")
treeRef.column("1", width=400)
treeRef.heading("2", text="Desc")
treeRef.column("2", width=100)
sb = tkinter.Scrollbar(genome_frame, orient="vertical", command=treeRef.yview)
sb.grid(row=3, column=5)
treeRef.configure(yscrollcommand=sb.set)

update_ref_genomes()
ref_button_frame = tkinter.Frame(genome_frame)
ref_button_frame.grid(row=4, column=0)

# Buttons
tkinter.Button(ref_button_frame, text="Add", command=selectRefGenomes).grid(row=0, column=0)
tkinter.Button(ref_button_frame, text="Remove", command=None).grid(row=0, column=1)
tkinter.Button(ref_button_frame, text="Refresh", command=update_ref_genomes).grid(row=0, column=3)

# Load probe frame
# **********************
probe_frame = tkinter.Frame(top, borderwidth=5, highlightbackground="black", highlightthickness=1)
probe_frame.grid(row=2, column=0, sticky="N", pady=10, padx=10)
tkinter.Label(probe_frame, text="Probe fasta file:").grid(row=0, column=0)
global file_path
file_path = tkinter.Label(probe_frame, text="")
file_path.grid(row=0, column=1)
probe_frame_button = tkinter.Frame(probe_frame)
probe_frame_button.grid(row=1, column=0)

# Buttons
tkinter.Button(probe_frame_button, text="Load", command=browsefunc).grid(row=0, column=0)
tkinter.Button(probe_frame_button, text="Remove", command=removeLoadedProbe).grid(row=0, column=1)

frame_btn_str = tkinter.Frame(top)
frame_btn_str.grid(row=0, column=1)
tkinter.Button(frame_btn_str, text="Start", command=start_scan).grid(row=0, column=0)
tkinter.Button(frame_btn_str, text="Stop", command=None).grid(row=0, column=1)
tkinter.Button(frame_btn_str, text="Exit", command=top.destroy).grid(row=0, column=2)

top.mainloop()
