# cryptoquizz

## Task Problem Statement:

```
Hello, young hacker. Are you ready to fight rogue machines ? Now, you'll have to prove us that you are a genuine cryptographer.
Running on quizz.teaser.insomnihack.ch:1031
```

## Path to solution:

I first tried to visit `quizz.teaser.insomnihack.ch:1031` from the browser but I got an ERR_INVALID_RESPONSE.

On doing `nc quizz.teaser.insomnihack.ch 1031`, I got the following response:

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~ Hello, young hacker. Are you ready to fight rogue machines ?    ~~
~~ Now, you'll have to prove us that you are a genuine             ~~
~~ cryptographer.                                                  ~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


~~ What is the birth year of Phil Rogaway ?
```

On running the same command again, the response asked for the birth year of some other guy.
For every run, a new name appeared, and in certain runs, previous names were repeated.

On entering the correct birth year of a cryptographer, I was asked the name of another cryptographer immediately.

Also, the connection was getting closed in around 2 seconds or so.
I wrote a script to see if I could find a complete list of names. There were only *44 names* which were being randomly selected.

My initial guess was that I'll have to send the correct birth years for all 44 people within 2 seconds. I didn't want to do
premature optimization so I just wrote a script to create a stream socket connection with the server and a send-recv loop
to get cryptographer names and send their birth years.

After 7 iterations, the server sent the flag:

```
'\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n~~ OK, young hacker. You are now considered to be a                ~~\n~~ INS{GENUINE_CRYPTOGRAPHER_BUT_NOT_YET_A_PROVEN_SKILLED_ONE}     ~~\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n'
```
