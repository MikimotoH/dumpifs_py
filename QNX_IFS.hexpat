#include <std/sys.pat>
#include <std/mem.pat>
#include <std/time.pat>

#pragma endian little

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

struct image_header {
	char   signature[7];		/* Image filesystem signature */
	u8		flags;				/* endian neutral flags */
	u32		image_size;			/* size from header to end of trailer */
	u32		hdr_dir_size;		/* size from header to last dirent */
	u32		dir_offset;			/* offset from header to first dirent */
	u32		boot_ino[4];		/* inode of files for bootstrap pgms */
	u32		script_ino;			/* inode of file for script */
	u32		chain_paddr;		/* offset to next filesystem signature */
	u32		spare[10];
	u32		mountflags;			/* default _MOUNT_* from sys/iomsg.h */
	char   mountpoint[dir_offset-88];			/* default mountpoint for image */
};

fn u32_to_timestr(u32 e){
  std::time::Time t = std::time::to_local(e);
  return std::time::format(t, "%Y-%m-%d %H:%M:%S");
};
using u32_time_t = u32[[format("u32_to_timestr")]];

fn u32_to_file_mode(u32 m){
  return std::format("0o{:07o}", m);
};
using u32_file_mode = u32[[format("u32_to_file_mode")]];


struct image_attr {
    u16		size;			/* size of dirent */
    u16		extattr_offset;	/* If zero, no extattr data */
    u32		ino;			/* If zero, skip entry */
    u32_file_mode		mode;			/* Mode and perms of entry */
    u32		gid;
    u32		uid;
    u32_time_t		mtime;
};

u32 	S_IFMT   = 0o00170000;
u32 	S_IFLNK   =0o0120000;
u32 	S_IFREG   =0o0100000;
u32 	S_IFDIR   =0o0040000;


//struct image_dir {						/* (attr.mode & S_IFMT) == S_IFDIR */
  //  image_attr	attr;
    //char path[attr.size-24];
//};

struct image_dirent{
  image_attr attr;
  if((attr.mode & S_IFDIR) == S_IFDIR){
      char path[attr.size-24];
  }
  else if((attr.mode & S_IFLNK) == S_IFLNK){
    u16 sym_offset;
    u16 sym_size;
    char sym_linkname[sym_offset];
    char sym_target[sym_size];    
    char __pad[attr.size - 28 - sym_offset - sym_size];
  }
  else if((attr.mode & S_IFREG) == S_IFREG){
     u32 offset;
     u32 size;
     char path[attr.size-32];
  }
};


startup_header startup_header_at_0xFA0 @ 0xFA0;
image_header image_header_at_0x890A8 @ 0x890A8;

image_dirent image_dirent_at_0x89104 @ 0x89104;
image_dirent image_dirent_at_0x89120 @ 0x89120;
image_dirent image_dirent_at_0x89178 @ 0x89178;