BITS 32

extern scanf
extern printf

section .rodata
	fmt: db "%d", 0
	output: db "%d is the ",0
	out_2:db "%d'th fibonacci number",10 ,0

section .text
	global main
	main:

	mov ebp, esp
	push ebp
	sub esp, 0x20

	lea eax, [ebp-0x4]
	push eax
	push fmt
	call scanf

	mov DWORD [ebp-0x8], 0
	cmp DWORD [ebp-0x4], 1
	mov eax, DWORD [ebp-0x8]
	je end



	mov DWORD [ebp-0x12], 1
	cmp DWORD [ebp-0x4], 2
	mov eax, [ebp-0x12]
	je end


	mov ecx, 3
	
	LOOP:

	mov eax, DWORD [ebp-0x8]
	add eax, DWORD [ebp-0x12]

	cmp ecx, DWORD [ebp-0x4]
	je end


	mov ebx, DWORD [ebp-0x12]
	mov DWORD [ebp-0x8], ebx
	mov DWORD [ebp-0x12], eax
	
	inc ecx
	jmp LOOP



	end:
		push eax
		push output
		call printf
		push DWORD[ebp-0x4]
		push out_2
		call printf
		ret