# Dogecoin faucet

This is an attempt to write a dogecoin faucet in Python.
*It's still in development.*

## (Planned) Dependencies

 - Python2 >=2.6 (Python 3?)
 - ( [block_io == 1.1.2](https://block.io/api/simple/python) ) not strictly necessary
 - sqlite3 (should be included in python)
 - requests (definitely >= 1.0, because Response.json() is called as a method)

## Planned functionality

- Request payment, store address in database
- Check if address is already in "waiting for payment" database
- Process payments (using block.io)
    * maybe create seperate PaymentProcessor class,
      to support diffent online (or private, via RPC) wallets

## License

I have not yet decided on a license, IANAL, but I somehow
lean towards GPL. No idea how this works for web applications
when it comes to the term "distribution".... Suggestions are 
welcome.
