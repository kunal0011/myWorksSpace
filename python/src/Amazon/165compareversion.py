class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_revisions = list(map(int, version1.split('.')))
        v2_revisions = list(map(int, version2.split('.')))

        # Determine the maximum length of the revisions
        max_length = max(len(v1_revisions), len(v2_revisions))

        # Compare each revision, treating missing revisions as 0
        for i in range(max_length):
            rev1 = v1_revisions[i] if i < len(v1_revisions) else 0
            rev2 = v2_revisions[i] if i < len(v2_revisions) else 0

            if rev1 < rev2:
                return -1
            if rev1 > rev2:
                return 1

        # If all revisions are equal
        return 0
