import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory_MNHN = file.parents [1]  # 0: meme niveau, 1: 1 niveau d'écart etc.
root_path = file.parents[2]
sys.path.append(str(package_root_directory_MNHN))


import MNHN.localNeighbour.localNeighbourfonction as localNeighbourfonction
import MNHN.utils.folder as folder

 
path_folder_fasta = f"{root_path}/DATA_MNHN/data_Result/Pfam_split/Pfam_train"  # data train
path_folder_pid = f"{root_path}/DATA_MNHN/PID"
list_residu = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", 
               "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]
path_CUBE = folder.creat_folder(f"{root_path}/DATA_MNHN/data_Result/Pfam_split/CUBE_2")


# cube -2,k
delay_num = -2
kp_SeqChoice = "k"
triplet_count, name_folder_fasta = localNeighbourfonction.multi_triplet_count_for_cube(path_folder_fasta, path_folder_pid, delay_num, kp_SeqChoice, list_residu, pid_inf = 62)
cond_proba, path_proba_cond = localNeighbourfonction.cube(triplet_count, name_folder_fasta, path_CUBE, delay_num, kp_SeqChoice, list_residu)
localNeighbourfonction.dico_visualisation(cond_proba)


# cube 2,k
delay_num = 2
kp_SeqChoice = "k"
triplet_count, name_folder_fasta = localNeighbourfonction.multi_triplet_count_for_cube(path_folder_fasta, path_folder_pid, delay_num, kp_SeqChoice, list_residu, pid_inf = 62)
cond_proba, path_proba_cond = localNeighbourfonction.cube(triplet_count, name_folder_fasta, path_CUBE, delay_num, kp_SeqChoice, list_residu)
localNeighbourfonction.dico_visualisation(cond_proba)



# cube -2,p
delay_num = -2
kp_SeqChoice = "p"
triplet_count, name_folder_fasta = localNeighbourfonction.multi_triplet_count_for_cube(path_folder_fasta, path_folder_pid, delay_num, kp_SeqChoice, list_residu, pid_inf = 62)
cond_proba, path_proba_cond = localNeighbourfonction.cube(triplet_count, name_folder_fasta, path_CUBE, delay_num, kp_SeqChoice, list_residu)
localNeighbourfonction.dico_visualisation(cond_proba)


# cube 2,p
delay_num = 2
kp_SeqChoice = "p"
triplet_count, name_folder_fasta = localNeighbourfonction.multi_triplet_count_for_cube(path_folder_fasta, path_folder_pid, delay_num, kp_SeqChoice, list_residu, pid_inf = 62)
cond_proba, path_proba_cond = localNeighbourfonction.cube(triplet_count, name_folder_fasta, path_CUBE, delay_num, kp_SeqChoice, list_residu)
localNeighbourfonction.dico_visualisation(cond_proba)