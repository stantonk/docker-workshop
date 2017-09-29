all: clean
	CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build wat.go
	docker build -t wat .

clean:
	rm -f wat
