import tkinter
from tkinter import *
from ttkwidgets import CheckboxTreeview
import loadAllGenomesIdsFromSQL
from DownloadUnzipManage import downlaod_genome, unzip_downloads
import load_downloaded_genomes


def selectRefGenomes(top_window):
    genomes_ids_data = loadAllGenomesIdsFromSQL.get_genomes_ids_csv()
    global select_win
    select_win = Toplevel(top_window)

    # Local genomes
    genome_frame = tkinter.Frame(select_win, borderwidth=5, highlightbackground="black", highlightthickness=1)
    genome_frame.grid(row=0, column=0, sticky="N", pady=10, padx=10)
    tkinter.Label(genome_frame, text="Local reference Genomes").grid(row=2, column=0)
    global tree_view_search
    tree_view_search = CheckboxTreeview(genome_frame, column=("1", "2"), show=("headings", "tree"))
    tree_view_search.grid(row=3, column=0)
    tree_view_search.heading("#0", text="ID")
    tree_view_search.column("#0", minwidth=0, width=60, stretch=YES)
    tree_view_search.heading("1", text="Name")
    tree_view_search.column("1", width=400)
    tree_view_search.heading("2", text="Comment")

    ref_button_frame = tkinter.Frame(genome_frame)
    ref_button_frame.grid(row=4, column=0)

    # Buttons
    tkinter.Button(ref_button_frame, text="Remove", command=selectRefGenomes).grid(row=0, column=0)
    tkinter.Button(ref_button_frame, text="Update", command=update_downloaded_genomes).grid(row=0, column=1)

    # Update downloaded genomes from local
    update_downloaded_genomes()
    # Download table
    download_genome_frame = tkinter.Frame(select_win, borderwidth=10, highlightbackground="black", highlightthickness=1)
    download_genome_frame.grid(row=0, column=1, sticky="N", pady=10, padx=10)
    tkinter.Label(download_genome_frame, text="Reference Genomes").grid(row=2, column=0)
    global tree_ref_sql
    tree_ref_sql = CheckboxTreeview(download_genome_frame, column=("1", "2"), show=("headings", "tree"))
    tree_ref_sql.heading("#0", text="GenomeID")
    tree_ref_sql.column("#0", minwidth=0, width=120, stretch=NO)
    tree_ref_sql.grid(row=3, column=0)
    tree_ref_sql.heading("1", text="Number")
    tree_ref_sql.column("1", width=80)
    tree_ref_sql.heading("2", text="Desc")
    tree_ref_sql.column("2", width=380)
    sb = tkinter.Scrollbar(download_genome_frame, orient="vertical", command=tree_ref_sql.yview)
    sb.grid(row=3, column=5)
    tree_ref_sql.configure(yscrollcommand=sb.set)

    ref_button_frame = tkinter.Frame(download_genome_frame)
    ref_button_frame.grid(row=4, column=0)

    # Buttons
    tkinter.Button(ref_button_frame, text="Download", command=downloads_checked).grid(row=1, column=0)
    tkinter.Button(ref_button_frame, text="Collapse", command=collapse).grid(row=1, column=1)
    global search_entry_query
    search_entry_query = tkinter.Entry(ref_button_frame)
    search_entry_query.grid(row=0, column=1)
    tkinter.Button(ref_button_frame, text="Search", command=search_genome_list).grid(row=0, column=2)

    # buttons on main frame
    main_btn_frame = tkinter.Frame(select_win)
    main_btn_frame.grid(row=2, column=1)
    tkinter.Button(main_btn_frame, text="Apply", command=None).grid(row=0, column=0)
    tkinter.Button(main_btn_frame, text="Close", command=select_win.destroy).grid(row=0, column=1)

    # Insert data into download window
    for index, key in enumerate(genomes_ids_data):
        tree_ref_sql.insert("", "end", index, text=key.split("_")[0], values=("", ""))
        genomes_df = genomes_ids_data[key]
        for i, row in genomes_df.iterrows():
            tree_ref_sql.insert(index, "end", str(index) + str(i), text=row['id'], values=(row['number'], row['desc']))


def collapse():
    tree_ref_sql.collapse_all()


def downloads_checked():
    item_list_checked = tree_ref_sql.get_checked()
    item_list = list(set(item_list_checked))
    genomes_ids_to_download = []
    for item in item_list:
        genome = tree_ref_sql.item(item)
        genome_id = genome['text']
        genomes_ids_to_download.append(genome_id)
    genomes_ids_to_download = list(set(genomes_ids_to_download))
    print(genomes_ids_to_download)
    for genome_id_to_download in genomes_ids_to_download:
        downlaod_genome.download_genome(genome_id_to_download)
    unzip_downloads.unzip()
    update_downloaded_genomes()


def update_downloaded_genomes():
    tree_view_search.delete(*tree_view_search.get_children())
    downloaded_items = load_downloaded_genomes.load_downloaded_genomes()
    for index, item in enumerate(downloaded_items):
        tree_view_search.insert("", "end", index, text=index, values=(item, "comment"))


def search_genomes():
    key_query = search_entry_query.get()
    print(key_query)
    i = 1
    for items in tree_ref_sql.get_children():
        child_list = tree_ref_sql.get_children(items)
        for child in child_list:
            tree_item_id = child
            genome_id = tree_ref_sql.item(child)['text']
            values = tree_ref_sql.item(child)['values']
            if len(key_query) > 0:
                if key_query in str(values[1]) or key_query == str(genome_id):
                    # print("Tree id:", tree_item_id, "Genome id:", genome_id, "Values", values)
                    tree_view_search_sub.insert("", "end", str(i), text=genome_id, values=(values[0], values[1]))
                    i += 1


def search_genome_list():
    search_win = Toplevel(select_win)
    search_win.title("Search genome")
    search_win.geometry("800x350")
    Button(search_win, text="Apply", command=check_searched_items).grid(row=2, column=3, pady=5)
    Button(search_win, text="Close", command=search_win.destroy).grid(row=2, column=4, pady=5)
    global tree_view_search_sub
    tree_view_search_sub = CheckboxTreeview(search_win, column=("1", "2"), show=("headings", "tree"))
    tree_view_search_sub.grid(row=3, column=1)
    tree_view_search_sub.heading("#0", text="ID")
    tree_view_search_sub.column("#0", minwidth=0, width=90, stretch=YES)
    tree_view_search_sub.heading("1", text="Number")
    tree_view_search_sub.column("1", width=100)
    tree_view_search_sub.heading("2", text="Description")
    tree_view_search_sub.column("2", width=400)
    search_genomes()


def check_searched_items():
    checked_searched_ids = []
    checked_search_items = tree_view_search_sub.get_checked()
    # gets all checked searched items
    if len(checked_search_items) > 0:
        for item_id in checked_search_items:
            checked_searched_ids.append(tree_view_search_sub.item(item_id)['text'])
    #           checks all searched items general list
    print(checked_searched_ids)
    check_items_per_id(checked_searched_ids)


def check_items_per_id(checked_ids):
    for id in checked_ids:
        for items in tree_ref_sql.get_children():
            child_list = tree_ref_sql.get_children(items)
            for child in child_list:
                tree_item_id = child
                genome_id = tree_ref_sql.item(child)['text']
                values = tree_ref_sql.item(child)['values']
                if genome_id == id:
                    # print("Found item")
                    # print(child)
                    # print(tree_ref_sql.item(child))
                    tree_ref_sql.change_state(child, "checked")
                    tree_ref_sql.change_state(items, "checked")


# top_test = tkinter.Tk()
#
# selectRefGenomes(top_test)
# top_test.mainloop()
