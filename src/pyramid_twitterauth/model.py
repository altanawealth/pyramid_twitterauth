# -*- coding: utf-8 -*-

"""Provides an SQLAlchemy based ``TwitterAccount`` model class."""

from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, Unicode
from sqlalchemy.orm import backref, relationship

from pyramid_basemodel import Base, BaseMixin, Session, save
from pyramid_simpleauth import model as simpleauth_model

_user_backref = backref("twitter_account", lazy="joined", uselist=False)

class TwitterAccount(Base, BaseMixin):
    """A user's twitter account with oauth token and access permission data."""
    
    __tablename__ = 'auth_twitter_accounts'
    
    twitter_id = Column(Integer, unique=True)
    screen_name = Column(Unicode(20))
    
    oauth_token = Column(Unicode(200))
    oauth_token_secret = Column(Unicode(200))
    access_permission = Column(Unicode(64))
    
    # XXX defines a relation to a table defined in `pyramid_simpleauth`.
    user_id = Column(Integer, ForeignKey('auth_users.id'))
    user = relationship(simpleauth_model.User, backref=_user_backref)
    
    def __json__(self):
        """Return a dictionary representation of the ``TwitterAccount`` instance.
          
              >>> account = TwitterAccount(twitter_id=1234, screen_name='thruflo')
              >>> account.__json__()
              {'twitter_id': 1234, 'screen_name': 'thruflo'}
          
        """
        
        return {'twitter_id': self.twitter_id, 'screen_name': self.screen_name}
    

