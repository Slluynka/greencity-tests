# Test Cases for GreenCity Events Page

---

##  Test Case 1: Display events list

### Preconditions:
- User opens the events page

### Test Steps:

| Step | Action | Data | Expected Result |
|-|--------|------|----------------|
| 1 | Open the events page | URL | Page loads successfully |
| 2 | Observe events list | — | List of events is displayed |
| 3 | Check event cards | — | Each event has title, date, and description |

---

##  Test Case 2: Open event details

### Preconditions:
- Events list is displayed

### Test Steps:

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Click on any event | Event card | Event details page opens |
| 2 | Check event information | — | Full information about event is displayed |
| 3 | Verify content | — | Title, date, description are visible |

---

##  Test Case 3: Navigation between pages

### Preconditions:
- User is on events page

### Test Steps:

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Scroll the page | — | Page scroll works correctly |
| 2 | Use navigation (if pagination exists) | Page number | New events are loaded |
| 3 | Reload page | — | Page reloads without errors |

---

## Negative Test Case 4: Offline filter shows both offline and online events

### Preconditions:
- User opens the events page
- Events list contains both "offline" and "online" events

### Test Steps:

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Open the events page | URL | Page loads successfully |
| 2 | Find filter section | — | Filters are visible |
| 3 | Apply filter "Offline" | Filter: Offline | Only offline events should be displayed |
| 4 | Observe events list | — |  Both offline and online events are displayed |

---

### Actual Result:
- Events list contains both offline and online events after applying "Offline" filter

### Expected Result:
- Only offline events should be displayed

### Status:
- Failed 

### Severity:
- Medium (filter functionality is broken)
