import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory_MNHN = file.parents [1]
root_path = file.parents[2]
sys.path.append(str(package_root_directory_MNHN))  


import MNHN.blosum.blosumfonction as blosumfonction
import MNHN.utils.folder as folder
import os


path_folder_fasta = f"{root_path}/DATA_MNHN/data_Result/Pfam_split/Pfam_train"   # chemin des seeds d'entrainement
name_folder_fasta =  os.path.basename(path_folder_fasta)
path_folder_pid = f"{root_path}/DATA_MNHN/PID"
list_residu = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", 
               "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]
#pid_inf = 62
#pid_inf = 50
#pid_inf = 30
pid_inf = 0
count_AA, nb_AA, count_coupleAA, nb_coupleAA = blosumfonction.multi_count_for_blosum(path_folder_fasta, path_folder_pid, list_residu, pid_inf)
path_non_contextual_result = f"{root_path}/DATA_MNHN/data_Result/Pfam_split/Context_Free_Pfam_train_pid_0"  # chemin à choisir
path_folder_Result = folder.creat_folder(path_non_contextual_result)
freq_AA, freq_coupleAA = blosumfonction.freq_for_blosum(count_AA, nb_AA, count_coupleAA, nb_coupleAA, path_folder_Result)


# blosum
blosum = blosumfonction.blosum_score(freq_AA, freq_coupleAA, path_folder_Result, scale_factor = 2)
# blosumfonction.blosum_visualisation(blosum)
# print("")
blosumfonction.blosum_visualisation_transposition(blosum)
title_heatmap = f"Heatmap of the Blosum variant computed on {name_folder_fasta}"
blosumfonction.blosum_heatmap(blosum, path_folder_Result, title_heatmap, size_annot = 5)

# Différence entre ma variante de blosum et une blosum de référence
pid_inf_ref = 62
matrix_diff, pid_inf_ref, average_diff = blosumfonction.blosum_difference(blosum, pid_inf_ref)

title_heatmap = f"Heatmap of the difference in Score between Blosum({name_folder_fasta}) and Blosum{pid_inf_ref}Ref\nThe mean difference is {average_diff}"
blosumfonction.blosum_heatmap(matrix_diff, path_folder_Result, title_heatmap, size_annot = 5)


# conditional proba
cond_proba = blosumfonction.blosum_conditional_proba(freq_AA, freq_coupleAA, path_folder_Result)
# blosumfonction.blosum_visualisation(cond_proba)
# blosumfonction.sum_line(cond_proba)
# print("")
blosumfonction.blosum_visualisation_transposition(cond_proba)
blosumfonction.sum_line_transposition(cond_proba)
title_heatmap = f"Heatmap of the conditional probability matrix computed on {name_folder_fasta}"
blosumfonction.blosum_heatmap(cond_proba, path_folder_Result, title_heatmap)