from datetime import datetime
from app.extensions import db

class Server(db.Model):
    """
    Server model.
    This class represents the Server object and its attributes, which are mapped to columns in a database table using SQLAlchemy.

    Args:
        db.Model: base class for all models.

    Attributes:
        id (db.Integer): primary key, unique identifier for each server.
        name (db.String): unique name of the server.
        description (db.String): description of the server.
        region (db.String): region of the server.
        verification_level (db.Integer): verification level of the server.
        default_message_notifications (db.Integer): default message notification level of the server.
        explicit_content_filter (db.Integer): explicit content filter level of the server.
        afk_channel_id (db.Integer): foreign key to the Channel table, representing the AFK channel of the server.
        afk_timeout (db.Integer): AFK timeout duration of the server.
        icon (db.String): icon URL of the server.
        banner (db.String): banner URL of the server.
        splash (db.String): splash URL of the server.
        system_channel_id (db.Integer): foreign key to the Channel table, representing the system channel of the server.
        system_channel_flags (db.Integer): system channel flags of the server.
        owner_id (db.Integer): foreign key to the User table, representing the owner of the server.
    """
    __tablename__ = 'servers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.String(255))
    region = db.Column(db.String(20), nullable=False, default='us-west')
    verification_level = db.Column(db.Integer, nullable=False, default=0)
    default_message_notifications = db.Column(db.Integer, nullable=False, default=0)
    explicit_content_filter = db.Column(db.Integer, nullable=False, default=0)
    afk_channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'))
    afk_timeout = db.Column(db.Integer, nullable=False, default=300)
    icon = db.Column(db.String(255))
    banner = db.Column(db.String(255))
    splash = db.Column(db.String(255))
    system_channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'))
    system_channel_flags = db.Column(db.Integer, nullable=False, default=0)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Member(db.Model):
    """
    Member model.
    This class represents the Member object and its attributes, which are mapped to columns in a database table using SQLAlchemy.

    Args:
        db.Model: base class for all models.

    Attributes:
        id (db.Integer): primary key, unique identifier for each member.
        username (db.String): unique username of the member.
        discriminator (db.String): unique discriminator of the member.
        avatar (db.String): the URL of the member's avatar image.
        joined_at (db.DateTime): the date and time the member joined the server.
        server_id (db.Integer): foreign key to the Server table, representing the server the member belongs to.
    """
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    discriminator = db.Column(db.String(4), nullable=False)
    avatar = db.Column(db.String(255))
    joined_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    server_id = db.Column(db.Integer, db.ForeignKey('servers.id'))

    def __repr__(self):
        return f'<Member {self.username}#{self.discriminator}>'