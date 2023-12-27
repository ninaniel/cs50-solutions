import requests
import sys

def main():
    try:
        bit = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        rate = o["bpi"]["USD"]["rate_float"]
        amount = bit * rate
        print(f"${amount:,.4f}")

    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")

    except requests.RequestException:
        pass


if __name__ == "__main__":
    main()