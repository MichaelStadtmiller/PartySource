# PARTY SOURCE 
## Project Description
ThePartySource.com offers a 10% discounts when a case is bought or you buy the remaining amount of a case.
_If they have 2 bottles left and you buy both - they will honor the 10% discount._
This script will scrape thepartysource.com for this information and present it meaningfully.

## Phases of Development

### Current Phase
Scraping information from a given product page.

### Next Phases
[ ] Gather products
  * give a search phrase to thepartysource.com
  * collect output into an array (in-stock and low-stock only)
2. Gather product details
  * cost,  liter amount (L), quantity on hand (QOH), type, brand, etc.
3. Analysis
  * calculate cost per bottle (CPB) after discount,  what's low? alternative comparison, etc.
4. User Input (override analysis with user input)
  * only search an sticker price range (filter out low and high end, etc.)
  * limit total amount to spend
  * limit total L to buy

### Future Phases
* Web App
* Mobile App