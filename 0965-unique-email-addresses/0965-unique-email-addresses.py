class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for string in emails:
            email = string.split('@')
            if email[0][0] == '+' or ".com" not in email[1]:
                continue
            new_email = email[0]
            if '+' in new_email:
                new_email = new_email[:new_email.index('+')]
            if '.' in new_email:
                new_email = new_email.replace('.','')
            new_email = new_email + '@' + email[1]
            unique.add(new_email)
        return len(unique)
                