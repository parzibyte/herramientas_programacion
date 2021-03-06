/*

    Programado por Luis Cabrera Benito 
  ____          _____               _ _           _       
 |  _ \        |  __ \             (_) |         | |      
 | |_) |_   _  | |__) |_ _ _ __ _____| |__  _   _| |_ ___ 
 |  _ <| | | | |  ___/ _` | '__|_  / | '_ \| | | | __/ _ \
 | |_) | |_| | | |  | (_| | |   / /| | |_) | |_| | ||  __/
 |____/ \__, | |_|   \__,_|_|  /___|_|_.__/ \__, |\__\___|
         __/ |                               __/ |        
        |___/                               |___/         
    
    
    Blog:       https://parzibyte.me/blog
    Ayuda:      https://parzibyte.me/blog/contrataciones-ayuda/
    Contacto:   https://parzibyte.me/blog/contacto/
*/
package main

import (
	"bytes"
	"crypto/sha512"
	"errors"
	"fmt"
	"golang.org/x/crypto/bcrypt"
)

func main() {
	fmt.Println(`HASHEAR CONTRASEÑAS CON BCRYPT Y SHA512

By Parzibyte
**************************
https://parzibyte.me/blog
**************************

`)

	fmt.Println("Escribe la contraseña plana: ")
	var passPlana string
	fmt.Scanln(&passPlana)
	hash, err := hashearPassword(passPlana)
	if err != nil {
		fmt.Printf("Error hasheando: %v", err)
	} else {
		fmt.Println("La contraseña hasheada es: ")
		fmt.Println(hash)
	}
	fmt.Println("\nPresiona ENTER para salir")
	fmt.Scanln(&passPlana)
}

func prepararPassPlana(passPlana string) string {
	passHasheada := sha512.Sum512_256([]byte(passPlana))
	hashSinNull := bytes.Trim(passHasheada[:], "\x00")
	return string(hashSinNull)
}

func hashearPassword(passPlana string) (string, error) {
	if len(passPlana) <= 0 {
		return "", errors.New("No se puede hashear una contraseña vacía")
	}
	//Al momento de escribir este código, bcrypt generaba un hash de 60 caracteres
	hash, err := bcrypt.GenerateFromPassword([]byte(prepararPassPlana(passPlana)), bcrypt.DefaultCost)
	if err != nil {
		return "", err
	}
	return string(hash), nil
}
