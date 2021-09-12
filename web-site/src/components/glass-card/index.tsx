import { ReactElement } from 'react';
import './index.scss';

interface IProps {
  children?: ReactElement | ReactElement[] | string | number | undefined;
  className?: string;
}

const GlassCard = (props: IProps) => {
  const { className = '', children } = props;
  return <div className={`glass-card ${className}`}>{children}</div>;
};

export default GlassCard;
