	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 14, 0	sdk_version 14, 2
	.globl	__ZN4Ansh6lengthEd              ; -- Begin function _ZN4Ansh6lengthEd
	.p2align	2
__ZN4Ansh6lengthEd:                     ; @_ZN4Ansh6lengthEd
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #16
	.cfi_def_cfa_offset 16
	str	x0, [sp, #8]
	str	d0, [sp]
	ldr	x8, [sp, #8]
	ldr	d0, [sp]
	str	d0, [x8, #8]
	movi	d0, #0000000000000000
	add	sp, sp, #16
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	__ZN4Ansh6squareEv              ; -- Begin function _ZN4Ansh6squareEv
	.p2align	2
__ZN4Ansh6squareEv:                     ; @_ZN4Ansh6squareEv
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #16
	.cfi_def_cfa_offset 16
	str	x0, [sp, #8]
	ldr	x8, [sp, #8]
	ldr	d0, [x8, #8]
	ldr	d1, [x8, #8]
	fmul	d0, d0, d1
	str	d0, [x8]
	movi	d0, #0000000000000000
	add	sp, sp, #16
	ret
	.cfi_endproc
                                        ; -- End function
.subsections_via_symbols
