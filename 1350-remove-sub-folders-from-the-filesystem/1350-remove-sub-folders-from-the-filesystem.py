class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder = sorted(folder)
        res = [folder[0]]

        for i in range(1, len(folder)):
            lf = res[-1]
            lf += '/'
            if not folder[i].startswith(lf):
                res.append(folder[i])
        return res