from typing import List

from sqlalchemy import String, Numeric, create_engine, select, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

class Base(DeclarativeBase):
    pass

class Investment(Base):
    __tablename__ = "investment"

    id: Mapped[int] = mapped_column(primary_key=True)
    coin: Mapped[str] = mapped_column(String(32))
    currency: Mapped[str] = mapped_column(String(3))
    amount: Mapped[float] = mapped_column(Numeric(5, 2))

    portfolio_id: Mapped[int] = mapped_column(ForeignKey("portfolio.id"))
    portfolio: Mapped["Portfolio"] = relationship(back_populates="investments")

    def __repr__(self) -> str:
        return f"<Investment coin: {self.coin}, currency: {self.currency}, amount: {self.amount}"
    
class Portfolio(Base):
    __tablename__ = "portfolio"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(Text())

    investments: Mapped[List["Investment"]] = relationship(back_populates="portfolio")

    def __repr__(self) -> str:
        return f"<Portfolio name: {self.name}"
    
engine = create_engine("sqlite:///demo_r.db")
Base.metadata.create_all(engine)

bitcoin = Investment(coin="bitcoin", currency="USD", amount=1.0)
ethereum = Investment(coin="ethereum", currency="GBP", amount=10.0)
dogecoin = Investment(coin="dogecoin", currency="EUR", amount=100.0)

portfolio_1 = Portfolio(name="Portfolio 1", description="Description 1")
portfolio_2 = Portfolio(name="Portfolio 2", description="Description 2")

bitcoin.portfolio = portfolio_1

with Session(engine) as session: 
    session.add(bitcoin)
    session.commit()