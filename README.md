# KultTarotBot
Very simple Python-based Discord bot for drawing Tarot cards in the Kult Divinity Lost roleplaying game.

Usage (in Discord): 
- `!tarot ?` - displays this message
- `!tarot` - generates 5 cards
- `!tarot n` - generates n cards (1-10)
- `!tarot n # comment` - adds a comment to the output
- `!tarot ?xxx` - lists card definitions for template xxx
- `!tarot xxx` - makes a 5 card draw for template xxx
- Templates: individuals (ind), locations (loc), cults (cul), plots (plo), creatures (cre) or artifacts (art)

### Bugs
- [x] ~Crescent card meanings incorrect~
- [ ] Fix extra colon in help message...

### Feature requests
- [x] ~Ability to add comment with tarot draw~
- [x] ~Help function via `!tarot ?`~
- [x] ~Change "state" to "Kult: !tarot ?"~
- [x] ~Add help for templates~
- [x] ~Add template draws~
- [x] ~Add comments for template draws~ 
- [ ] Dual tarot/dice calls
