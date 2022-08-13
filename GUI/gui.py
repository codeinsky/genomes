import tkinter
from ttkwidgets import CheckboxTreeview
from tkinter import filedialog
import guiSelectRefGenome
top = tkinter.Tk()
top.geometry('1000x400')


def browsefunc():
    filename = filedialog.askopenfilename(filetypes=(("fasta files", "*.fasta"), ("All files", "*.*")))
    file_path.config(text=filename)
    print(filename)


def removeLoadedProbe():
    file_path.config(text="")


def selectRefGenomes():
    guiSelectRefGenome.selectRefGenomes(top)


#  Genome frame
# *********************************************
genome_frame = tkinter.Frame(top, borderwidth=5, highlightbackground="black", highlightthickness=1)
genome_frame.grid(row=0, column=0, sticky="N", pady=10, padx=10)
tkinter.Label(genome_frame, text="Reference genome list").grid(row=2, column=0)
treeRef = CheckboxTreeview(genome_frame, column=("1", "2"), show=("headings", "tree"))
treeRef.grid(row=3, column=0)
treeRef.heading("1", text="Name")
treeRef.heading("2", text="Comment")
treeRef.insert("", "end", "1", text="1")
treeRef.insert("", "end", "2", text="2")

ref_button_frame = tkinter.Frame(genome_frame)
ref_button_frame.grid(row=4, column=0)

# Buttons
tkinter.Button(ref_button_frame, text="Add", command=selectRefGenomes).grid(row=0, column=0)
tkinter.Button(ref_button_frame, text="Remove", command=None).grid(row=0, column=1)

# Load probe frame
# **********************
probe_frame = tkinter.Frame(top, borderwidth=5, highlightbackground="black", highlightthickness=1)
probe_frame.grid(row=0, column=2, sticky="N", pady=10, padx=10)
tkinter.Label(probe_frame, text="Probe fasta file:").grid(row=0, column=0)
file_path = tkinter.Label(probe_frame, text="c:fasta.fa")
file_path.grid(row=0, column=1)
probe_frame_button = tkinter.Frame(probe_frame)
probe_frame_button.grid(row=1, column=0)

# Buttons
tkinter.Button(probe_frame_button, text="Load", command=browsefunc).grid(row=0, column=0)
tkinter.Button(probe_frame_button, text="Remove", command=removeLoadedProbe).grid(row=0, column=1)

frame_btn_str = tkinter.Frame(top)
frame_btn_str.grid(row=0, column=1)
tkinter.Button(frame_btn_str, text="Start", command=None).grid(row=0, column=0)
tkinter.Button(frame_btn_str, text="Stop", command=None).grid(row=0, column=1)

top.mainloop()
