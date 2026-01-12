Overview
This artefact presents a high-level object-oriented architecture design for an online shopping system called ShopEase. The purpose of the design is to demonstrate how layered architecture and modular design can support scalability, maintainability, and security in an e-commerce system.

Architecture style
The system is designed using a layered architecture with three main layers: the presentation layer, the business logic layer, and the data access layer. Each layer has a clear responsibility and communicates only with the layer directly below it.

Presentation layer
The presentation layer handles user interaction through a web or mobile interface. It is responsible for receiving user requests, performing basic input validation, and returning responses. This layer does not contain business rules or direct database access.

Business logic layer
The business logic layer contains the core functionality of the system. This includes user authentication, product searching and browsing, shopping cart management, order processing, and payment handling. Business rules are implemented here using object-oriented principles such as encapsulation and polymorphism.

Data access layer
The data access layer is responsible for storing and retrieving data from the database. It abstracts database operations away from the business logic layer and provides controlled access to data related to users, products, and orders.

Key modules
The system is divided into logical modules including user management, product catalogue, and order processing. Each module has a clearly defined responsibility and interacts with other modules through well-defined interfaces.

Scalability and extensibility
The design supports scalability by separating concerns into independent modules. New features, such as additional payment methods or recommendation engines, can be added by extending existing abstractions rather than modifying core system logic.

Security considerations
Security is addressed primarily within the business logic layer. Authentication and authorisation are handled centrally, sensitive data is not exposed to the presentation layer, and input validation is performed to reduce security risks.

Reflection
This design demonstrates how object-oriented architecture can support system growth and safe change over time. Although the artefact does not represent a production-ready implementation, it illustrates how layered separation and abstraction improve maintainability, extensibility, and security in large-scale software systems.
