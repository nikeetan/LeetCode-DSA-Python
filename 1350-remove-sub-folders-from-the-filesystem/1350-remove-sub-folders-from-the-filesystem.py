class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder_set = set(folder)
        res = []

        for f in folder:
            is_sub = False
            prefix = f

            while prefix and (not(is_sub)):
                
                print("Before",prefix)
                pos = prefix.rfind("/")
                
                prefix = prefix[0 : pos]
                print("After",prefix)
    
                if prefix in folder_set:
                    is_sub = True

            if is_sub == False:
                res.append(f)
            
        return res