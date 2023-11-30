From: Eric
Subject: RE: URGENT ISSUE WITH PRODUCTION!!!!

Hi Carrie,

Thank you for raising this - it sounds like some of your records are too large for your plan. There are two ways to fix this issue:

- [only send attributes necessary for searching](https://www.algolia.com/doc/guides/sending-and-managing-data/prepare-your-data/how-to/reducing-object-size/#remove-unused-attributes)
- [use smaller records and enable the 'distinct' feature on the index](https://www.algolia.com/doc/guides/sending-and-managing-data/prepare-your-data/how-to/indexing-long-documents/)

If you leverage these strategies, not only is this going to stop the errors your users are observing, but their searches will be more relevant, since there will be less text in each record.

Please let me know if leveraging these strategies resolves this issue and improves your users' experience.

Best,

Eric
