import os
path = '/Users/momo/Desktop/micdata_gen/'

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.png'):
            if root.endswith('mic_unwarping'):
                aroot = root.replace('mic_unwarping', 'mic_warping')  # 此时root仍未mic_unwarping
                tmp_unwarping = os.path.join(root, file)
                tmp_warping = os.path.join(root.replace('mic_unwarping', 'mic_warping'), file)
                assert (os.path.exists(tmp_warping)), "error"
                print(tmp_warping)
                i = i+1
                fp = open('/Users/momo/Desktop/micdata_gen/lm_path.txt', 'a')
                fp.write(tmp_warping)
                fp.write('\n')