from sys import argv
import copy

son_small = [[0 for i in range(26)] for i in range(300005)]
haslength_small = [[0 for i in range(25)] for i in range(300005)]
is_word_small = [0 for i in range(300000)]
son_large = [[0 for i in range(26)] for i in range(300005)]
haslength_large = [[0 for i in range(30)] for i in range(300005)]
is_word_large = [0 for i in range(300000)]
ans = ['' for i in range(16)]
word_number = 0

def BuildTrie(small_list, large_list):

	global son_small
	global son_large
	global haslength_large
	global haslength_small
	global is_word_large
	global is_word_small

	file1 = open(small_list, 'r')
	file2 = open(large_list, 'r')
	tot = 1
	for l in file1:
		word_len = len(l) - 1
		#print('filename= ', small_list,'l= ', len(l), 'word_len= ', word_len)
		now = 1
		for kk in range(word_len):
			haslength_small[now][word_len] = 1
			#print('now= ', now, ' l[kk]= ', l[kk])
			if son_small[now][ord(l[kk]) - ord('a')] == 0:
				tot += 1
				son_small[now][ord(l[kk]) - ord('a')] = tot
			#print(now, ' ', ord(l[kk]) - ord('a'), ' ', l)
			now = son_small[now][ord(l[kk]) - ord('a')]
		haslength_small[now][word_len] = 1
		is_word_small[now] = 1
	for l in file2:
		word_len = len(l) - 1
		now = 1
		for kk in range(word_len):
			#print('now= ', now, 'l= ', l)
			haslength_large[now][word_len] = 1
			if son_large[now][ord(l[kk]) - ord('a')] == 0:
				tot += 1
				son_large[now][ord(l[kk]) - ord('a')] = tot
			now = son_large[now][ord(l[kk]) - ord('a')]
		haslength_large[now][word_len] = 1
		is_word_large[now] = 1



def DfsSmall1(mat, step, word_number, quiz_number):

	global ans

	out_ans = ''
	if step == word_number + 1:
		ans_number[quiz_number] += 1
		for ii in range(1, word_number):
			out_ans += ans[ii] + ' '
		out_ans += ans[word_number]
		print(out_ans)
		out_ans = ''
		return
	aa = ''
	for ii in range(j):
		for jj in range(j):
			if (mat[ii][jj] != 0) and (son_small[1][ord(mat[ii][jj]) - ord('a')] != 0) and (s[step][0] == '*' or s[step][0] == mat[ii][jj]):
				DfsSmall2(ii, jj, mat, step, 1, aa + mat[ii][jj], son_small[1][ord(mat[ii][jj]) - ord('a')])




def DfsSmall2(x, y, mat, step, now, temp, current):

	if haslength_small[current][length[step]] == 0:
		return
	pre = mat[x][y]
	mat[x][y] = 0
	if now == len(s[step]):
		nex = [[0 for iii in range(16)] for iii in range(16)]
		for jjj in range(j):
			tt = j
			for iii in range(j - 1, -1, -1):
				if mat[iii][jjj] != 0:
					nex[tt][jjj] = mat[iii][jjj]
					tt -= 1
		ans[step] = temp
		if is_word_small[current] == 1:
			DfsSmall1(nex, step + 1, word_number, quiz_number)
		mat[x][y] = pre
		return

	for fx in range(-1, 2):
		for fy in range(-1, 2):
			if fx != 0 or fy != 0:
				nex = x + fx
				ney = y + fy
				if nex < 0 or nex >= j or ney < 0 or ney >= j:
					continue
				if mat[nex][ney] == 0:
					continue
				if s[step][now] != '*' and s[step][now] != mat[nex][ney]:
					continue
				if son_small[current][ord(mat[nex][ney]) - ord('a')] == 0:
					continue
				DfsSmall2(nex, ney, mat, step, now + 1, temp + mat[nex][ney], son_small[current][ord(mat[nex][ney]) - ord('a')])
	mat[x][y] = pre
	return




def WordSolver(puzzle_file, ouput_file):

	global word_number
	global j
	global s
	global length
	global quiz_number

	f = open(puzzle_file, 'r')
	data = []
	i = 0
	quiz_number = 1
	ans_number = [0, 0]
	for l in f:
		data.append(l.strip('\n'))
	while i < len(data):
		s = []
		length = []
		mat = [[0 for j in range(16)] for j in range(16)]
		j = len(data[i])
		#print(data)
		for k in range(j):
			for q in range(j):
				mat[k][q] = data[i + k][q]
		print(mat)
		i += k
		i += 1
		s = data[i].split()
		word_number = len(s)
		for k in s:
			length.append(len(k))
		DfsSmall1(mat, 1, word_number, quiz_number)
		#if ans_number[quiz_number] == 0:
		#	DfsLarge1(mat, 1, word_number, quiz_number)
		print('.')
		i += 1
		quiz_number += 1
		ans_number.append(0)



if __name__ == "__main__":
	filename1 = argv[1]
	filename2 = argv[2]
	filename3 = argv[3]
	filename4 = argv[4]
	BuildTrie(filename1, filename2)
	WordSolver(filename3, filename4)