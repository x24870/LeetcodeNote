package main

import (
	"crypto/md5"
)

type Codec struct {
	s2l     map[string]string
	l2s     map[string]string
	counter int
}

func Constructor() Codec {
	return Codec{
		s2l:     make(map[string]string),
		l2s:     make(map[string]string),
		counter: 0,
	}
}

// Encodes a URL to a shortened URL.
func (this *Codec) encode(longUrl string) string {
	shortUrl, ok := this.l2s[longUrl]
	if ok {
		return shortUrl
	}

	shortUrlByte := md5.Sum([]byte(longUrl))
	shortUrl = string(shortUrlByte[:])
	this.l2s[longUrl] = shortUrl
	this.s2l[shortUrl] = longUrl
	return shortUrl
}

// Decodes a shortened URL to its original URL.
func (this *Codec) decode(shortUrl string) string {
	return this.s2l[shortUrl]
}

/**
 * Your Codec object will be instantiated and called as such:
 * obj := Constructor();
 * url := obj.encode(longUrl);
 * ans := obj.decode(url);
 */
