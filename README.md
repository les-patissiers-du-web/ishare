# Ishare

A simple command line tool for sharing files

## Usage

### To install

```bash
python setup.py install
```

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

## TODO

- [x] Convert into a Python executable module
- [ ] Remove configuration from script to dotfiles in user $HOME
- [ ] Support key authentication
- [ ] Support HTTP POST for upload
- [ ] Improve upload and url generation for filename with multiple . (ex: .tar.gz)
- [ ] Add list command
- [x] Add progression bar
- [ ] Create a simple cronjob to delete files
- [ ] Add security for private folder (auto / specific password)
- [ ] Add a parameter for TTL
- [ ] Installation instruction
- [ ] Python3 compatibility

## Development

### Build container

```bash
docker build -t ishare .
```

### Run container

```bash
docker run --rm --name ishare-test -i -t -v $PWD:/app ishare sh
```
