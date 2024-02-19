// image.h

typedef u32 u32;
typedef u16 u16;
typedef unsigned char u8;


#define __FLEXARY(__type, __name) __type __name[1]

enum {
	IMAGE_FLAGS_BIGENDIAN	= 0x01,	/* header, trailer, dirents in big-endian format  */
	IMAGE_FLAGS_READONLY	= 0x02,	/* do not try to write to image (rom/flash) */
	IMAGE_FLAGS_INO_BITS	= 0x04	/* inode bits valid */
};

u32 	S_IFMT   =00170000;
u32 	S_IFSOCK  =0140000;
u32 	S_IFLNK   =0120000;
u32 	S_IFREG   =0100000;
u32 	S_IFBLK   =0060000;
u32 	S_IFDIR   =0040000;
u32 	S_IFCHR   =0020000;
u32 	S_IFIFO   =0010000;
u32 	S_ISUID   =0004000;
u32 	S_ISGID   =0002000;
u32 	S_ISVTX   =0001000;

#define IMAGE_SIGNATURE		"imagefs"


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
	char   mountpoint[1];			/* default mountpoint for image */
};

struct image_attr {
    u16		size;			/* size of dirent */
    u16		extattr_offset;	/* If zero, no extattr data */
    u32		ino;			/* If zero, skip entry */
    u32		mode;			/* Mode and perms of entry */
    u32		gid;
    u32		uid;
    u32		mtime;
};

struct image_file {						/* (attr.mode & S_IFMT) == S_IFREG */
    struct image_attr	attr;
    u32		offset;			/* Offset from header */
    u32		size;
    __FLEXARY(char, path);				/* null terminated path (No leading slash) */
};

struct image_dir {						/* (attr.mode & S_IFMT) == S_IFDIR */
    struct image_attr	attr;
    __FLEXARY(char, path);				/* null terminated path (No leading slash) */
};

struct image_symlink {					/* (attr.mode & S_IFMT) == S_IFLNK */
    struct image_attr	attr;
    u16		sym_offset;
    u16		sym_size;
    __FLEXARY(char, path);				/* null terminated path (No leading slash) */
    /*	char				sym_link[1];*/	/* symlink contents */
};

struct image_device {					/* (attr.mode & S_IFMT) == S_IFCHR|BLK|FIFO|NAM|SOCK */
    struct image_attr	attr;
    u32		dev;
    u32		rdev;
    __FLEXARY(char, path);				/* null terminated path (No leading slash) */
};
