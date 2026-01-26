# MedTrack OSS Architecture

## Overview
MedTrack OSS follows a decoupled architecture with a FastAPI backend and multiple frontend options (Astro/React and Vanilla JS).

## Components
1. **FastAPI Backend**: Handles business logic, authentication, and data persistence.
2. **MongoDB**: Stores user profiles, medication details, and adherence logs.
3. **Redis & Celery**: Manages asynchronous notification tasks and reminder scheduling.
4. **Notification Service**: Pluggable interface for SMS (Twilio), Email (SMTP), and Push.

## Data Flow
1. User creates a medication schedule.
2. Backend stores schedule and triggers a Celery task.
3. Celery task wakes up at scheduled time and sends notification.
4. User logs dose taken via Frontend.
5. Adherence metrics updated in DB.
