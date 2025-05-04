javascript:(function() {
  function createDialog() {
    const overlay = document.createElement('div');
    overlay.style = `
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background-color: rgba(0, 0, 0, 0.6);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 999999;
      font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    `;

    const modal = document.createElement('div');
    modal.style = `
      background-color: #262626;
      color: white;
      border-radius: 13px;
      width: 310px;
      overflow: hidden;
      box-shadow: 0 10px 30px rgba(0,0,0,0.85);
      font-size: 14px;
    `;

    const content = document.createElement('div');
    content.style = 'padding: 20px 16px; text-align: center;';

    const title = document.createElement('div');
    title.textContent = 'Action restricted';
    title.style = 'font-size: 16px; font-weight: 600; margin-bottom: 6px;';
    content.appendChild(title);

    const subtitle = document.createElement('div');
    subtitle.textContent = `Your account has been temporarily locked due to suspicious activity. You will be logged out. Try again in 5 minutes.`;
    subtitle.style = 'font-size: 13px; color: #a9a9a9; line-height: 1.4;';
    content.appendChild(subtitle);

    modal.appendChild(content);

    const divider = () => {
      const line = document.createElement('div');
      line.style = 'height: 1px; background: #3a3a3c;';
      return line;
    };

    const logoutBtn = document.createElement('div');
    logoutBtn.textContent = 'Log out';
    logoutBtn.style = `
      padding: 13px 0;
      color: #ff3b30;
      font-weight: 600;
      text-align: center;
      cursor: pointer;
      font-size: 16px;
    `;
    logoutBtn.onclick = () => {
      window.location.href = 'https://www.instagram.com/accounts/logout/';
    };

    const cancelBtn = document.createElement('div');
    cancelBtn.textContent = 'Cancel';
    cancelBtn.style = `
      padding: 13px 0;
      color: white;
      text-align: center;
      cursor: pointer;
      font-size: 16px;
    `;
    cancelBtn.onclick = () => {
      document.body.removeChild(overlay);
      setTimeout(() => createDialog(), 1000);
    };

    modal.appendChild(divider());
    modal.appendChild(logoutBtn);
    modal.appendChild(divider());
    modal.appendChild(cancelBtn);

    overlay.appendChild(modal);
    document.body.appendChild(overlay);
  }

  createDialog();
})();
