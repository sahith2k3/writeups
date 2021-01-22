BITS 32

extern printf
extern scanf

section .rodata
	fmt: db "%d", 0
	sum_out: db "sum is %d", 10 ,0
	sub_out: db "difference is %d", 10, 0
	mul_out: db "product is %d", 10, 0
	div_out: db "quotient is %d ",0
	divr_out:db "and remainder is %d", 10, 0
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

	lea edx, [ebp-0x8]
	push edx
	push fmt
	call scanf

	;adding
	mov ebx, dword [ebp-0x4]
	mov eax, dword [ebp-0x8]
	add eax, ebx
	mov dword [ebp-0x12], eax

	push dword [ebp-0x12]
	push sum_out
	call printf

	;subtracting
	mov ebx, dword [ebp-0x8]
        mov eax, dword [ebp-0x4]
	sub eax, ebx
	mov dword [ebp-0x12], eax

	push dword [ebp-0x12]
	push sub_out
	call printf

	;multiplying

        mov eax, dword [ebp-0x8]
	mul dword [ebp-0x4]
	mov dword [ebp-0x12], eax

	push dword [ebp-0x12]
	push mul_out
	call printf

	;dividing
	xor edx, edx
	mov eax, [ebp-0x4]
	div dword [ebp-0x8]
	mov dword [ebp-0x12], eax

	push dword [ebp-0x12]
	push div_out
	call printf

	mov dword [ebp-0x12], edx
	push dword [ebp-0x12]
	push divr_out
	call printf

	leave
	ret

