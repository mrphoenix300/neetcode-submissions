class Solution:

    def encode(self, strs: List[str]) -> str:
        strs_tmp = [string for string in strs]
        check_again = False
        # if len(strs) <= 1:
        #     if strs[0] == "":
        #         return ""
        encoded_strs = ""
        for string in strs_tmp:
            if string:
                for c in string:
                    encoded_strs += chr(ord(c) + 5)
            else:
                encoded_strs += "*"
            encoded_strs += "_"
        
        return encoded_strs if len(strs) >= 1 else "0"

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        elif s == "0":
            return []
        s_tmp = s[:]
        print(s)

        decoded_strs = []
        encoded_strs = list(filter(None, s_tmp.split("_")))
        for string in encoded_strs:
            decoded_string = ""
            if string != "*":
                for c in string:
                    decoded_string += chr(ord(c) - 5)
            decoded_strs.append(decoded_string)
        
        return decoded_strs
                
