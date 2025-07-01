# Week11_Reflection.md

## 📌 Section 0: Fellow Details

| Field              | Your Entry        |
|-------------------|-------------------|
| Name              | Samantha Shuler-Pomeroy |
| GitHub Username   | SamPomeroy        |
| Preferred Feature Track | Interactive    |
| Team Interest     | Yes — Contributor / Technical Mentor Hybrid |

---

## ✍️ Section 1: Week 11 Reflection

**Key Takeaways**
- Capstone is structured with core expectations plus creative freedom via features.
- Week-by-week pacing helps avoid overwhelm.
- Architecture planning is as important as implementation.
- MVC/layered approaches are emphasized for maintainability.
- Peer collaboration and modularity are encouraged.

**Concept Connections**
- Strongest: API integration, data processing, modular architecture (MVC), debugging.
- Needs more practice: Tkinter GUI styling, testing strategies, packaging for release.

**Early Challenges**
- None major — already have OpenWeatherMap API key and folder setup experience.
- Needed to align project expectations with structured class pace.

**Support Strategies**
- I’ll use office hours for any GUI structure issues or feature integrations.
- Slack for quick syntax or config help.
- Classmates can help sanity-check architecture ideas or test features.

---

## 🧠 Section 2: Feature Selection Rationale

| #  | Feature Name     | Difficulty | Why You Chose It / Learning Goal |
|----|------------------|------------|----------------------------------|
| 1  | Favorite Cities  | ⭐⭐         | Practice persistent storage and switching between inputs |
| 2  | Weather Alerts   | ⭐⭐         | Implement user-based conditional logic |
| 3  | Weather Journal  | ⭐⭐         | Add interactivity and user-generated data |
|    | **Enhancement**  | –          | Personality / chatbot-style interaction |

---

## 🗂️ Section 3: High-Level Architecture Sketch

**Modules**
- `core/` — API handler, file storage, config
- `features/` — Journal, Alerts, Favorites
- `gui/` — Tkinter UI components
- `main.py` — App entrypoint & coordinator

**Data Flow**
- GUI sends user input → controller
- Controller fetches weather via API module
- Processed data flows to GUI + features
- Features log/save data to local files

---

## 📊 Section 4: Data Model Plan

| File/Table Name     | Format | Example Row                          |
|---------------------|--------|--------------------------------------|
| weather_history.txt | txt    | 2025-06-09,New Brunswick,78,Sunny    |
| favorites.json      | json   | { "home": "New Brunswick", "work": "Jersey City" } |
| journal_entries.csv | csv    | 2025-06-09,Cloudy,Feeling lazy       |
| alerts_config.json  | json   | { "high_temp": 90, "low_temp": 35 } |

---

## 📆 Section 5: Personal Project Timeline

| Week | Monday         | Tuesday        | Wednesday     | Thursday       | Key Milestone         |
|------|----------------|----------------|----------------|----------------|------------------------|
| 12   | API setup      | Error handling | Tkinter shell | Buffer day     | Basic working app      |
| 13   | Feature 1      |                | Integrate      |                | Feature 1 complete     |
| 14   | Feature 2 start|                | Review & test  | Finish         | Feature 2 complete     |
| 15   | Feature 3      | Polish UI      | Error passing  | Refactor       | All features complete  |
| 16   | Enhancement    | Docs           | Tests          | Packaging      | Ready-to-ship app      |
| 17   | Rehearse       | Buffer         | Showcase       | –              | Demo Day               |

---

## ⚠️ Section 6: Risk Assessment

| Risk             | Likelihood | Impact | Mitigation Plan                                 |
|------------------|------------|--------|--------------------------------------------------|
| API Rate Limit   | Medium     | Medium | Add delay, use caching, avoid unnecessary calls |
| GUI Complexity   | Medium     | Low    | Start basic, test incrementally                 |
| Feature Overlap  | Low        | Medium | Clarify integration logic early                 |

---

## 🤝 Section 7: Support Requests

- None for now — I’ve been managing my own pace well using structured guidance and tools.
- Will ask for GUI-specific input or Tkinter issues if needed.
- Peer feature review may help with usability checks.

---

## ✅ Section 8: Before Monday Checklist

- [x] Pushed `main.py`, `config.py`, and `/data/` folder
- [x] `.env` has API key (excluded from commit)
- [x] Feature templates copied into `/features/`
- [x] Drafted README.md
- [x] Architecture and planning complete

🗓️ Created: 2025-06-25