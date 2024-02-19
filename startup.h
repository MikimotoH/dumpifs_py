// startup.c

typedef unsigned int u32;
typedef unsigned short u16;
typedef unsigned char u8;


struct startup_header {
	u32	signature;			/*I  Header sig, see below*/
	u16	version;			/*I  Header vers, see below*/
	u8	flags1;				/*IS Misc flags, see below*/
	u8	flags2;             /*   No flags defined yet*/
	u8	header_size;		/*S  sizeof(struct startup_header)*/
	u8	machine;			/*IS Machine type from sys/elf.h*/
	u32	startup_vaddr;		/*I  Virtual Address to transfer*/
										/*   to after IPL is done*/
	u32	paddr_bias;			/*S  Value to add to physical address*/
										/*   to get a value to put into a*/
										/*   pointer and indirected through*/
	u32	image_paddr;		/*IS Physical address of image*/
	u32	ram_paddr;			/*IS Physical address of RAM to copy*/
										/*   image to (startup_size bytes copied)*/
	u32	ram_size;			/*S  Amount of RAM used by the startup*/
										/*   program and executables contained*/
										/*   in the file system*/
	u32	startup_size;		/*I  Size of startup (never compressed)*/
	u32	stored_size;		/*I  Size of entire image*/
	u32	imagefs_paddr;		/*IS Set by IPL to where the imagefs is when startup runs*/
	u32	imagefs_size;		/*S  Size of uncompressed imagefs*/
	u16	preboot_size;		/*I  Size of loaded before header*/
	u16	zero0;				/*   Zeros */
	u8	zero[3];			/*   Zeros */
	u8	info[48];			/*IS Array of startup_info* structures*/
};
