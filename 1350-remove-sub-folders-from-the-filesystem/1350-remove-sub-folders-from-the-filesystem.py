class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder_set = set(folder)
        res = []

        for f in folder:
            is_sub = False
            prefix = f

            while prefix:
                
                pos = prefix.rfind("/")

                if pos == -1:
                    break
                prefix = prefix[0 : pos]
    
                if prefix in folder_set:
                    is_sub = True
            if is_sub == False:
                res.append(f)
            
        return res