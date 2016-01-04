# Ishare

A simple command line tool for sharing files

## Usage

### To push a file

```
$ ishare filename.ext
Uploading: filename.ext
Password:
I share: https://domain.tld/public/2506e40747c1e4fe1c8c42037083a6ac80d10e34/filename.ext

$ ishare --private filename.ext
Uploading: filename.ext
Password:
I share: https://domain.tld/private/2506e40747c1e4fe1c8c42037083a6ac80d10e34/filename.ext
```

### To delete a file

```
$ ishare --delete public/2506e40747c1e4fe1c8c42037083a6ac80d10e34/filename.ext
Deleting: public/2506e40747c1e4fe1c8c42037083a6ac80d10e34/filename.ext
Password: 
public/2506e40747c1e4fe1c8c42037083a6ac80d10e34
/var/www/public/2506e40747c1e4fe1c8c42037083a6ac80d10e34
Deleted
```
