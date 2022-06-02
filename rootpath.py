import sys  
from pathlib import Path  
file = Path(__file__).resolve()  
package_root_directory_MNHN = file.parents[1]
sys.path.append(str(package_root_directory_MNHN))
print(package_root_directory_MNHN)