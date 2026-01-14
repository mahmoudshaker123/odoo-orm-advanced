# 🚀 Odoo ORM & Backend Development Training

This repository is a **hands-on training project** to deeply understand **Odoo Backend Development** with a strong focus on **ORM methods, business logic, and real-world use cases**.

The goal is not just to "make things work", but to understand **how Odoo works internally**, how to write **clean, secure, and scalable code**, and how to think like a professional **Odoo Developer**.

---

## 📌 Odoo Version
- **Odoo 18**

---

## 🎯 Training Objectives

- Master **Odoo ORM lifecycle**
- Write **business-driven logic**, not just technical code
- Understand **performance, security, and best practices**
- Prepare for **Odoo Developer technical interviews**
- Build a strong **GitHub portfolio**

---

## 🧠 Topics Covered

### 1️⃣ Odoo ORM Fundamentals
- `create()`
- `write()`
- `unlink()`
- `copy()`
- `search()`
- `browse()`
- `filtered()`
- `mapped()`

📌 Focus:
- Recordsets
- Multi-record operations
- Database vs in-memory operations
- Performance considerations

---

### 2️⃣ Record Lifecycle & Business Logic
- Overriding ORM methods:
  - `create`
  - `write`
  - `unlink`
  - `copy`
- Validations & constraints:
  - `@api.constrains`
  - Business validation inside `write`
- Difference between:
  - ORM validation
  - SQL constraints

---

### 3️⃣ Computed Fields & Onchange
- `@api.depends`
- Stored vs non-stored computed fields
- `@api.onchange`
- When to use **onchange vs compute**
- UI behavior vs database persistence

---

### 4️⃣ Default Values & Display Logic
- `default_get()`
- Context-based defaults
- `name_get()`
- `name_search()`
- How records are displayed and searched in Many2one fields

---

### 5️⃣ Odoo Views (UI Layer)
- Form View
- Tree (List) View
- Search View
- Kanban View
- Calendar View
- Pivot & Graph Views

📌 Advanced Topics:
- Dynamic readonly / invisible fields
- Header buttons
- Statusbar
- View inheritance
- XML parsing & external IDs

---

### 6️⃣ Wizards (Transient Models)
- `models.TransientModel`
- Wizard lifecycle
- Popup actions (`target="new"`)
- Passing data using context
- Wizards for:
  - Filtering data
  - Creating records
  - Bulk updates
  - Reports (PDF / Excel)

---

### 7️⃣ Smart Buttons & Actions
- Smart buttons in form views
- Related records counters
- `ir.actions.act_window`
- Context & domain usage
- Real business scenarios (Tasks, Contracts, Logs…)

---

### 8️⃣ Security & Access Control
- `ir.model.access.csv`
- Record Rules
- ACL vs Record Rules
- Multi-user testing
- Avoiding overuse of `sudo()`

---

### 9️⃣ Reports
- QWeb PDF Reports
- QWeb HTML Reports
- XLSX Reports
- Passing data from Wizards to Reports
- Business reporting use cases

---

### 🔟 Performance & Best Practices
- Domain optimization
- Avoiding `filtered()` on large datasets
- Indexing fields
- Stored fields performance impact
- Logging vs print
- Clean code principles in Odoo

---

### 1️⃣1️⃣ API & Integration (Basics)
- JSON controllers
- REST-style endpoints
- External API consumption
- Secure data exposure

---

## 🧪 Training Methodology

- Each topic includes:
  - ✅ Simple example
  - 🏢 Real business use case
  - 🐞 Debugging with `pdb` & logs
  - ❌ Common mistakes
  - ⭐ Best practices

- Code is written as if it were:
  - Production-ready
  - Reviewed by a senior developer
  - Used in a real company

---

## 🏗️ Example Business Domain

The training uses a **Task Management domain**, similar to real Odoo modules:
- Tasks
- Categories
- Users
- States
- Reports
- Wizards

This makes the learning process **practical and realistic**.

---

## 🎓 Target Audience

- Junior Odoo Developers
- Backend Developers transitioning to Odoo
- Developers preparing for **Odoo technical interviews**
- Anyone who wants to understand **Odoo deeply**, not superficially

---

## 🧩 Why This Repository?

Most tutorials show *how* to do things.  
This repository focuses on **why** things work the way they do in Odoo.

> "Understanding Odoo internals is what separates a junior developer from a professional one."

---

## 🧑‍💻 Author
**Mahmoud Shaker**  
Backend & Odoo Developer  
Focused on clean code, business logic, and scalable systems.

---

## 🚀 Next Steps
- Add unit tests
- Advanced security scenarios
- Performance optimization cases
- Real interview-style coding challenges

---

⭐ If you find this repository useful, feel free to star it!
