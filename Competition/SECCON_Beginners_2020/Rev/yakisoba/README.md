#### 作成日: 2021/03/01

# [Rev] yakisoba

## Description:

## Hints:
You'd better automate your analysis  

## Solution:

まずはfileコマンドでファイル形式を確認。  

	$ file yakisoba
	yakisoba: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=fc0031f79ea88d284f3177f980b40110c2612f3e, stripped  

ELFファイルを実行してみる。  

	$ ./yakisoba
	FLAG: 

Flag(文字列)入力が求められる。とりあえず適当な値を入れる。  

	FLAG: hello
	Wrong!
	$

案の定弾かれることを確認。

続いてstringsで中身を見てみる。  

	$ strings yakisoba
	/lib64/ld-linux-x86-64.so.2
	(O1w
	libc.so.6
	__printf_chk
	__isoc99_scanf
	puts
	__stack_chk_fail
	__cxa_finalize
	__libc_start_main
	GLIBC_2.7
	GLIBC_2.3.4
	GLIBC_2.4
	GLIBC_2.2.5
	_ITM_deregisterTMCloneTable
	__gmon_start__
	_ITM_registerTMCloneTable
	D$(1
	T$(dH3
	ctPv.
	>t_v=
	tRw?
	Yt>v,
	}tpv*
	stKv0
	pthvM
	Bt)v.
	t%v0
	At=v+
	tthvM
	1tFv+
	1t]vG
	ptKv0
	rtFv+
	ntCw(
	Wt%v0
	}t)vv
	AWAVI
	AUATL
	[]A\A]A^A_
	FLAG:
	%31s
	Wrong!
	Correct!
	;*3$"
	GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0
	.shstrtab
	.interp
	.note.ABI-tag
	.note.gnu.build-id
	.gnu.hash
	.dynsym
	.dynstr
	.gnu.version
	.gnu.version_r
	.rela.dyn
	.rela.plt
	.init
	.plt.got
	.text
	.fini
	.rodata
	.eh_frame_hdr
	.eh_frame
	.init_array
	.fini_array
	.dynamic
	.data
	.bss
	.comment

引数が誤っていたらWrong, 正しければCorrectを返すようである。  

なので、Correctに分岐するためにangrを利用する。  
何も考えずにこのプログラム[solve.py](solver/solve.py)を走らせる。  


2~3分ほどでFLAGを取得できる。  

