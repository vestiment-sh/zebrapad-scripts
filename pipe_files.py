import os 

txt_num = 1
path = 'D:/2.TextMining/S_CB_audio/piped_trans/cb_transcripts_token_final'
os.chdir(path)

for txt in os.listdir(path):
    with open(txt, 'r', encoding= 'utf-8') as f:
        content = f.readlines()
        for line in content:
            line = line.replace("', '",'|')
            outfile = open("D:/2.TextMining/S_CB_audio/piped_trans/cb_transcripts_token_final_ final/"+ f'{txt}'+".txt",'w', encoding= 'utf-8')
            outfile.writelines(line)
            txt_num += 1