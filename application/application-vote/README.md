# Voting App

A simple distributed application running across multiple Docker containers. This solution uses Python, Node.js, .NET, with Redis for messaging and Postgres for storage.


## Getting started


Run in this directory to build and run the app:

```shell
docker compose up -d
```

The `vote` app will be running at [http://localhost:5000](http://localhost:5000), and the `results` will be at [http://localhost:5001](http://localhost:5001).

To stop it
```shell
docker compose down
```
 
## Architecture diagram

![Architecture diagram](architectureDesign.png)

* A front-end web app in [Python](/vote) which lets you vote between two options
* A [Redis](https://hub.docker.com/_/redis/) which collects new votes
* A [.NET](/worker/) worker which consumes votes and stores them in a Postgres db
* A [Postgres](https://hub.docker.com/_/postgres/) database backed by a Docker volume
* A [Node.js](/result) web app which shows the results of the voting in real time

## Notes

The voting application only accepts one vote per client browser. It does not register additional votes if a vote has already been submitted from a client.
