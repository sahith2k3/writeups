BITS 32

extern scanf
extern printf

section .rodata
	fmt: db "%d", 0
	output_prime: db "%d is a prime number", 10, 0
	output_n: dw "%d is not a prime number", 10, 0

section .text
	global main

	main:
	mov ebp, esp
	push ebp
	sub esp, 0x8

	lea eax, [ebp-0x4]
	push eax
	push fmt
	call scanf

	mov ecx, 2
	primer:
	mov eax, DWORD [ebp-0x4]
	xor edx,edx
	div ecx
	cmp edx, 0
	je not_prime
	inc ecx
	cmp ecx, DWORD [ebp-0x4]
	je prime
	jmp primer


	prime:
	push DWORD[ebp-0x4]
	push output_prime
	call printf
	ret

	not_prime:
	push DWORD[ebp-0x4]
	push output_n
	call printf
	ret
	

