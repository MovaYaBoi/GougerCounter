{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e230d2bd-4d3d-4727-9db1-6bf612c5f80b",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import time\n",
    "from selenium import webdriver\n",
    "# For using Chrome\n",
    "browser = webdriver.Chrome('/Users/integ/anaconda3/envs/gpu_buy_bot/chromedriver.exe')\n",
    "\n",
    "# Bestbuy RTX 3060 Ti page\n",
    "browser.get(\"https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402\")\n",
    "\n",
    "buyButton = False\n",
    "\n",
    "while not buyButton:\n",
    "    try:\n",
    "        # If this works then the button is not pytopen\n",
    "        addToCartBtn = addButton = browser.find_element_by_class_name(\"btn-disabled\")\n",
    "        \n",
    "        # Button isnt open restart the script\n",
    "        print(\"Button isn't ready yet.\")\n",
    "        \n",
    "        # Refresh page afer a delay\n",
    "        time.sleep(1)\n",
    "        browser.refresh\n",
    "        \n",
    "    except:\n",
    "        addToCartBtn = addButton = browser.find_element_by_class_name(\"btn-primary\")\n",
    "        \n",
    "        #Click the button and end the script\n",
    "        print(\"Button was clicked\")\n",
    "        addToCartBtn.click()\n",
    "        buyButton = True\n",
    "\n",
    "goToCartButton = False\n",
    "\n",
    "while not goToCartButton:\n",
    "    try:\n",
    "        # If this works then the button is not pytopen\n",
    "        goToCartButton = cartButton = browser.find_element_by_class_name(\"btn-secondary\")\n",
    "        \n",
    "        # Button isnt open restart the script\n",
    "        print(\"Button isn't ready yet.\")\n",
    "        \n",
    "        # Refresh page after a delay\n",
    "        time.sleep(1)\n",
    "        browser.refresh\n",
    "    \n",
    "    except:\n",
    "        # Click the button and end the script\n",
    "        print(\"Button was clicked\")\n",
    "        goToCartButton.click()\n",
    "        goToCartButton = True\n",
    "        \n",
    "# Bestbuy Cart\n",
    "browser.get(\"https://www.bestbuy.com/cart\")\n",
    "        \n",
    "checkoutButton = False\n",
    "\n",
    "while not checkoutButton:\n",
    "    try:\n",
    "        # If this works then the button is not pytopen\n",
    "        checkoutButton = checkout = browser.find_element_by_class_name(\"btn-primary\")\n",
    "        \n",
    "        # Button isnt open restart the script\n",
    "        print(\"Button isn't ready yet.\")\n",
    "        \n",
    "        # Refresh page after a delay\n",
    "        time.sleep(1)\n",
    "        browser.refresh\n",
    "        \n",
    "    except:\n",
    "        # Click the button and end the script\n",
    "        print(\"Button was clicked\")\n",
    "        checkoutButton.click()\n",
    "        checkoutButton = True\n",
    "        \n",
    "# Bestbuy Payment\n",
    "browser.get(\"https://www.bestbuy.com/checkout/r/fulfillment\")\n",
    "\n",
    "fulfillmentButton = False\n",
    "\n",
    "while not fulfillmentButton:\n",
    "    try:\n",
    "        # If this works then the button is not pytopen\n",
    "        fulfillmentButton = fulfillment = browser.find_element_by_class_name(\"btn-secondary\")\n",
    "        \n",
    "        # Button isnt open restart the script\n",
    "        print(\"Button isn't ready yet.\")\n",
    "        \n",
    "        # Refresh page after a delay\n",
    "        time.sleep(1)\n",
    "        browser.refresh\n",
    "\n",
    "    except:\n",
    "        # Click the button and end the script\n",
    "        print(\"Button was clicked\")\n",
    "        fulfillmentButton.click()\n",
    "        fulfillmentButton = True\n",
    "        \n",
    "# Bestbuy Payment\n",
    "browser.get(\"https://www.bestbuy.com/checkout/r/payment\") \n",
    "\n",
    "paymentButton = False\n",
    "\n",
    "while not paymentButton:\n",
    "    try:\n",
    "        # If this works then the button is not pytopen\n",
    "        paymentButton = payment = browser.find_element_by_class_name(\"btn-primary\")\n",
    "        \n",
    "        # Button isnt open restart the script\n",
    "        print(\"Button isn't ready yet.\")\n",
    "        \n",
    "        # Refresh page after a delay\n",
    "        time.sleep(1)\n",
    "        browser.refresh\n",
    "    except:\n",
    "        #Click the button and end the script\n",
    "        print(\"Button was clicked\")\n",
    "        paymentButton.click()\n",
    "        paymentButton = True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f847f7c4-3eff-4d20-b33b-90a25dbf1a94",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
